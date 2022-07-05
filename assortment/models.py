from django.conf import settings
from django.db import models


class RecommendedMatrix(models.Model):
    created_at = models.DateTimeField(verbose_name='Создано', auto_created=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True, null=True, blank=True)
    # params
    category = models.IntegerField(verbose_name='Категория', null=True, blank=True)  # scan_and_train.Categories
    manufacturer = models.IntegerField(verbose_name='Производитель', null=True, blank=True)  # scan_and_train.Manufacturers (через scu)
    # filters
    retailer = models.IntegerField(verbose_name='Ритейлер', null=True, blank=True)  # recognizer_api.Storenetworks
    store_type = models.IntegerField(verbose_name='Тип магазина', null=True, blank=True)  # recognizer_api.Storetypes
    region = models.IntegerField(verbose_name='Регион', null=True, blank=True)  # recognizer_api.Regions
    store = models.CharField(verbose_name='Мазагин', null=True, blank=True, max_length=255)  # recognizer_api.Stores.address

    class Meta:
        verbose_name = 'Рекомендованная матрица'
        verbose_name_plural = 'Рекомендованные матрицы'


class ContractMatrix(models.Model):
    CREATED = 1
    ACTIVE = 2
    EXPIRED = 3

    STATUS_CHOICES = (
        (CREATED, 'Новая'),
        (ACTIVE, 'Активная (действующая)'),
        (EXPIRED, 'Истекшая'),
    )
    author = models.ForeignKey(
        verbose_name='Автор', related_name='contract_matrix', to=settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL,
    )
    status = models.SmallIntegerField(verbose_name='Статус матрицы', choices=STATUS_CHOICES, default=CREATED)
    start_dt = models.DateTimeField(verbose_name='Дата начала действия', auto_created=True, null=True, blank=True)
    end_dt = models.DateTimeField(verbose_name='Дата окончания действия', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Создано', auto_created=True, null=True, blank=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True, null=True, blank=True)
    category = models.IntegerField(verbose_name='Категория', null=True, blank=True)
    manufacturer = models.IntegerField(verbose_name='Производитель', null=True, blank=True)
    retailer = models.IntegerField(verbose_name='Ритейлер', null=True, blank=True)
    store_type = models.IntegerField(verbose_name='Тип магазина', null=True, blank=True)
    region = models.IntegerField(verbose_name='Регион', null=True, blank=True)
    store = models.CharField(verbose_name='Магазин', null=True, blank=True, max_length=255)
    recommended_matrix = models.ForeignKey(
        verbose_name='Рекомендованная матрица', to=RecommendedMatrix, on_delete=models.SET_NULL,
        related_name='contract_matrix', null=True, blank=True
    )

    class Meta:
        verbose_name = 'Контрактная матрицы'
        verbose_name_plural = 'Контрактные матрицы'


class RecommendedAssortment(models.Model):
    matrix = models.ForeignKey(to=RecommendedMatrix, null=True, blank=True, on_delete=models.CASCADE, related_name='assortment')
    barcode = models.CharField(null=True, blank=True, max_length=50) #scan_and_train.Scu.barcode
    scu = models.CharField(null=True, blank=True, max_length=255) #scan_and_train.Scu_id
    distribution = models.FloatField(null=True, blank=True) #рассчитаем
    facing_amount = models.FloatField(null=True, blank=True) #рассчитаем

    class Meta:
        verbose_name = 'Ассортимент рекомендованной матрицы'
        verbose_name_plural = 'Ассортименты рекомендованных матриц'


class ContractAssortment(models.Model):
    matrix = models.ForeignKey(to=ContractMatrix, null=True, blank=True, on_delete=models.CASCADE, related_name='assortment')
    barcode = models.CharField(null=True, blank=True, max_length=50)
    scu = models.CharField(null=True, blank=True, max_length=255)
    target_facings = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ассортимент контрактной матрицы'
        verbose_name_plural = 'Ассортименты контрактных матриц'