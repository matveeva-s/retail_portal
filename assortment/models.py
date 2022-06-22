from django.conf import settings
from django.db import models


class ContractMatrix(models.Model):
    CREATED = 1
    ACTIVE = 2
    EXPIRED = 3

    STATUS_CHOICES = (
        (CREATED, 'Новая'),
        (ACTIVE, 'Активная (действующая)'),
        (EXPIRED, 'Истекшая'),
    )
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.SmallIntegerField('Статус матрицы', choices=STATUS_CHOICES, null=True, blank=True)
    start_dt = models.DateTimeField(auto_created=True, null=True, blank=True)
    end_dt = models.DateTimeField(auto_created=True, null=True, blank=True)
    #params
    category = models.IntegerField(null=True, blank=True) #scan_and_train.Categories
    manufacturer = models.IntegerField(null=True, blank=True)  # scan_and_train.Manufacturers (через scu)
    #filters
    store_type = models.IntegerField(null=True, blank=True) #recognizer_api.Storetypes
    region = models.IntegerField(null=True, blank=True) #recognizer_api.Regions
    address = models.CharField(null=True, blank=True) #recognizer_api.Stores.address
    retailer = models.IntegerField(null=True, blank=True)  # recognizer_api.Storenetworks

    class Meta:
        verbose_name = 'Контрактная матрицы'
        verbose_name_plural = 'Контрактные матрицы'


class Assortment(models.Model):
    contact_matrix = models.ForeignKey(to=ContractMatrix, null=True, blank=True, on_delete=models.CASCADE)
    barcode = models.CharField(null=True, blank=True) #scan_and_train.Scu.barcode
    scu = models.CharField(null=True, blank=True) #scan_and_train.Scu_id
    distribution = models.IntegerField(null=True, blank=True) # рассчитаем
    facing_amount = models.IntegerField(null=True, blank=True) # рассчитаем

    class Meta:
        verbose_name = 'Ассортимент'
        verbose_name_plural = 'Ассортименты'