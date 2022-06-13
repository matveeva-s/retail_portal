from rest_framework import serializers
from recognizer_api.models import (
    Visits, Categories, Visitequipments, Visitbays, Visitshelves,
    Visitshelfemptyspaces, Visitshelfproducts, Visitshelfpricetags,
)
from scan_and_train.models import Sku


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

    class Meta:
        model = Visitequipments
        fields = (
            'id', 'bays'
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
