from collections import Counter

from django.db.models import Q
from rest_framework import serializers

from recognizer_api.models import (
    Visits, Categories, Visitequipments, Visitbays, Visitshelves,
    Visitshelfemptyspaces, Visitshelfproducts, Visitshelfpricetags,
    Storetypes, Regions, Stores, Storenetworks,
)
from scan_and_train.models import Sku

from recognizer_api.helpers import round_with_precision


class VisitsSerializer(serializers.ModelSerializer):
    store_address = serializers.SerializerMethodField()
    store_city = serializers.SerializerMethodField()
    store_type = serializers.SerializerMethodField()
    store_retailer = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    completion_date = serializers.SerializerMethodField()

    def get_store_address(self, instance):
        return instance.storeid.address

    def get_store_city(self, instance):
        return instance.storeid.cityid.name

    def get_store_type(self, instance):
        return instance.storeid.storetypeid.name

    def get_store_retailer(self, instance):
        return instance.storeid.storenetworkid.name

    def get_category(self, instance):
        equipment = instance.visitequipments_set.last()
        if not equipment or not equipment.supercategoryid:
            return None
        category_id = instance.visitequipments_set.first().supercategoryid
        try:
            name = Categories.objects.using('recognizer').get(id=category_id).name
            return name
        except Categories.DoesNotExist:
            return None

    def get_completion_date(self, instance):
        return instance.completiondate

    class Meta:
        model = Visits
        fields = (
            'id', 'userid', 'store_address', 'store_city', 'store_type',
            'completion_date', 'store_retailer', 'category'
        )


class PriceTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitshelfpricetags
        fields = (
            'id', 'x1', 'x2', 'y1', 'y2', 'height', 'width', 'value', 'confidence',
        )


class ProductSerializer(serializers.ModelSerializer):
    classifier = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    verification_status = serializers.SerializerMethodField()

    def get_classifier(self, product):
        return product.categoryproductclassifierversion

    def get_category_id(self, product):
        return product.supercategoryid

    def get_verification_status(self, product):
        return product.verificationstatus

    class Meta:
        model = Visitshelfproducts
        fields = (
            'id', 'x1', 'x2', 'y1', 'y2', 'height', 'width',
            'barcode', 'correctbarcode', 'category_id',
            'verification_status', 'classifier', 'confidence',
        )


class EmptyPlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visitshelfemptyspaces
        fields = (
            'id', 'x1', 'x2', 'y1', 'y2'
        )


class VisitShelfSerializer(serializers.ModelSerializer):
    empty_spaces = EmptyPlaceSerializer(source='visitshelfemptyspaces_set', many=True)
    products = ProductSerializer(source='visitshelfproducts_set', many=True)
    price_tags = PriceTagSerializer(source='visitshelfpricetags_set', many=True)

    class Meta:
        model = Visitshelves
        fields = (
            'id', 'x1', 'x2', 'y1', 'y2', 'empty_spaces', 'products', 'price_tags',
        )


class VisitBaysSerializer(serializers.ModelSerializer):
    shelves = VisitShelfSerializer(source='visitshelves_set', many=True)

    class Meta:
        model = Visitbays
        fields = (
            'id', 'shelves', 'photolink'
        )


class VisitEquipmentsSerializer(serializers.ModelSerializer):
    bays = VisitBaysSerializer(source='visitbays_set', many=True)
    category = serializers.SerializerMethodField()

    def get_category(self, equipment):
        try:
            name = Categories.objects.using('recognizer').get(id=equipment.supercategoryid).name
            return name
        except Categories.DoesNotExist:
            return None

    class Meta:
        model = Visitequipments
        fields = (
            'id', 'equipmenttypeid', 'category', 'bays',
        )


class VisitSerializer(serializers.ModelSerializer):
    photolinks = serializers.SerializerMethodField()
    completion_date = serializers.SerializerMethodField()
    equipments = VisitEquipmentsSerializer(source='visitequipments_set', many=True)

    def get_photolinks(self, instance):
        return instance.visitequipments_set.filter(
            visitbays__photolink__isnull=False
        ).values_list('visitbays__photolink', flat=True)

    def get_completion_date(self, instance):
        return instance.completiondate

    class Meta:
        model = Visits
        fields = (
            'id', 'photolinks', 'completion_date', 'equipments',
        )


class VisitProductsSerializer(serializers.ModelSerializer):
    photo_link = serializers.CharField(source='photolink')
    short_name = serializers.CharField(source='shortname')
    brand = serializers.SerializerMethodField()

    def get_brand(self, instance):
        return instance.brandid.title if instance.brandid else None

    class Meta:
        model = Sku
        fields = (
            'id', 'barcode', 'photo_link', 'short_name', 'brand',
        )


class StoreTypesOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storetypes
        fields = (
            'id', 'name',
        )


class RegionsOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regions
        fields = (
            'id', 'name',
        )


class StorenetworksOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Storenetworks
        fields = (
            'id', 'name',
        )


class AddressOptionsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='address')

    class Meta:
        model = Stores
        fields = (
            'id', 'name',
        )


class AssortmentSerializer(serializers.ModelSerializer):
    short_name = serializers.CharField(source='shortname')
    distribution = serializers.SerializerMethodField()
    facing_amount = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.qs = self.context.pop('_qs')

    def get_product_visits(self, product):
        return self.qs.filter(
            Q(
                visitequipments__visitbays__visitshelves__visitshelfproducts__barcode=product.barcode,
                visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode__isnull=True,
            ) |
            Q(visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode=product.barcode)
        ).distinct()

    def get_distribution(self, product):
        qset = self.get_product_visits(product)
        return round_with_precision(qset.count() / self.qs.distinct().count())

    def get_facing_amount(self, product):
        qset = self.get_product_visits(product)
        qset_facings = qset.values_list('visitequipments__visitbays__visitshelves__visitshelfproducts', flat=True)
        facings = 0
        if qset_facings.exists():
            facings = (qset_facings.count()) / (qset.count())
        return round_with_precision(facings)

    class Meta:
        model = Sku
        fields = (
            'id', 'barcode', 'short_name', 'name', 'distribution', 'facing_amount'
        )
