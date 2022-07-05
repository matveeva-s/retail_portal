from django.db.models import Q
from rest_framework import serializers

from recognizer_api.models import (
    Storetypes, Regions, Stores, Storenetworks,
)
from scan_and_train.models import Sku
from recognizer_api.helpers import round_with_precision
from assortment.models import RecommendedAssortment, ContractMatrix, ContractAssortment, RecommendedMatrix


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


class MatrixAssortmentSerializer(serializers.ModelSerializer):
    short_name = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    def get_short_name(self, assortment):
        return Sku.objects.using('scan_and_train').get(id=assortment.scu).shortname

    def get_name(self, assortment):
        return Sku.objects.using('scan_and_train').get(id=assortment.scu).name

    class Meta:
        model = RecommendedAssortment
        fields = (
            'id', 'barcode', 'short_name', 'name', 'distribution', 'facing_amount'
        )


class ContractMatrixReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.get_full_name')
    store_type = serializers.SerializerMethodField()
    retailer = serializers.SerializerMethodField()
    region = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    start_dt = serializers.SerializerMethodField()
    end_dt = serializers.SerializerMethodField()

    def get_store_type(self, matrix):
        return Storetypes.objects.using('recognizer').get(id=matrix.store_type).name

    def get_retailer(self, matrix):
        return Storenetworks.objects.using('recognizer').get(id=matrix.retailer).name

    def get_region(self, matrix):
        return Regions.objects.using('recognizer').get(id=matrix.region).name

    def get_address(self, matrix):
        store = Stores.objects.using('recognizer').get(id=matrix.store)
        return f'{store.cityid.name}, {store.address}'

    def get_start_dt(self, matrix):
        return matrix.start_dt.strftime('%d.%m.%y')

    def get_end_dt(self, matrix):
        return matrix.end_dt.strftime('%d.%m.%y')

    class Meta:
        model = ContractMatrix
        fields = (
            'id', 'author', 'retailer', 'store_type', 'region', 'address', 'start_dt', 'end_dt'
        )


class ContactAssortmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContractAssortment
        fields = (
            'barcode', 'scu', 'target_facings',
        )


class ContractMatrixSerializer(serializers.ModelSerializer):
    retailer = serializers.CharField(required=False)
    store_type = serializers.CharField(required=False)
    region = serializers.CharField(required=False)
    store = serializers.CharField(required=False)
    assortment = ContactAssortmentSerializer(required=False, many=True)
    start_dt = serializers.DateField(format='%d.%m.%Y')
    end_dt = serializers.DateField(format='%d.%m.%Y', required=False)
    recommended_matrix = serializers.PrimaryKeyRelatedField(queryset=RecommendedMatrix.objects.all(), required=False, allow_null=True)

    def create(self, validated_data):
        assortment = validated_data.pop('assortment')
        author = self.context['request'].user
        matrix = ContractMatrix.objects.create(**validated_data, author=author)
        assortment_list = []
        for product in assortment:
            assortment_list.append(
                ContractAssortment(
                    matrix=matrix, barcode=product['barcode'],
                    scu=product['scu'], target_facings=product['target_facings'],
                )
            )
        ContractAssortment.objects.bulk_create(assortment_list)
        return matrix

    class Meta:
        model = ContractMatrix
        fields = (
            'retailer', 'store_type', 'region', 'store', 'assortment', 'start_dt', 'end_dt', 'recommended_matrix'
        )
