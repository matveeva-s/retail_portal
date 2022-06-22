# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attributevalues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    value = models.TextField(db_column='Value', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    skuid = models.ForeignKey('Sku', models.DO_NOTHING, db_column='SkuId')  # Field name made lowercase.
    nameid = models.ForeignKey('Attributes', models.DO_NOTHING, db_column='NameId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttributeValues'


class Attributes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attributes'


class Augmenttasks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    augmentationid = models.IntegerField(db_column='AugmentationId', blank=True, null=True)  # Field name made lowercase.
    processed = models.BooleanField(db_column='Processed', blank=True, null=True)  # Field name made lowercase.
    finished = models.BooleanField(db_column='Finished', blank=True, null=True)  # Field name made lowercase.
    result = models.TextField(db_column='Result', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipfilename = models.TextField(db_column='ZipFileName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    augmentedpercent = models.FloatField(db_column='AugmentedPercent')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    datasetid = models.IntegerField(db_column='DataSetId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    skuids = models.TextField(db_column='SkuIds', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AugmentTasks'


class Augmentationsetitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nameid = models.IntegerField(db_column='NameId')  # Field name made lowercase.
    percent = models.IntegerField(db_column='Percent')  # Field name made lowercase.
    augmentationsetid = models.ForeignKey('Augmentationsets', models.DO_NOTHING, db_column='AugmentationSetId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AugmentationSetItems'


class Augmentationsets(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AugmentationSets'


class Boundboxes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1')  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2')  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1')  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2')  # Field name made lowercase.
    photoid = models.ForeignKey('Photos', models.DO_NOTHING, db_column='PhotoId', blank=True, null=True)  # Field name made lowercase.
    imagefromrecognizerid = models.ForeignKey('Imagefromrecognizers', models.DO_NOTHING, db_column='ImageFromRecognizerId', blank=True, null=True)  # Field name made lowercase.
    skuid = models.IntegerField(db_column='SKUId', blank=True, null=True)  # Field name made lowercase.
    ismain = models.BooleanField(db_column='IsMain')  # Field name made lowercase.
    cordx1 = models.IntegerField(db_column='CordX1')  # Field name made lowercase.
    cordx2 = models.IntegerField(db_column='CordX2')  # Field name made lowercase.
    cordy1 = models.IntegerField(db_column='CordY1')  # Field name made lowercase.
    cordy2 = models.IntegerField(db_column='CordY2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BoundBoxes'


class Brands(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Brands'


class Categories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    englisname = models.TextField(db_column='EnglisName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    skuquantity = models.IntegerField(db_column='SkuQuantity', blank=True, null=True)  # Field name made lowercase.
    formfactorsquantity = models.IntegerField(db_column='FormFactorsQuantity', blank=True, null=True)  # Field name made lowercase.
    scenariosquantity = models.IntegerField(db_column='ScenariosQuantity', blank=True, null=True)  # Field name made lowercase.
    pointsquantity = models.IntegerField(db_column='PointsQuantity', blank=True, null=True)  # Field name made lowercase.
    timequantity = models.IntegerField(db_column='TimeQuantity', blank=True, null=True)  # Field name made lowercase.
    classifieroutput = models.TextField(db_column='ClassifierOutput', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    errorpercent = models.IntegerField(db_column='ErrorPercent', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    inwork = models.IntegerField(db_column='InWork', blank=True, null=True)  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.
    readyforlearn = models.IntegerField(db_column='ReadyForLearn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'


class Categoriestoequipments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categoriesid = models.IntegerField(db_column='CategoriesId')  # Field name made lowercase.
    equipmentsid = models.IntegerField(db_column='EquipmentsId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoriesToEquipments'


class Changeitemrecords(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    changeid = models.IntegerField(db_column='ChangeId')  # Field name made lowercase.
    changevalue = models.TextField(db_column='ChangeValue', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changephotorecordid = models.ForeignKey('Changephotorecords', models.DO_NOTHING, db_column='ChangePhotoRecordId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChangeItemRecords'


class Changephotorecords(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    changedate = models.DateTimeField(db_column='ChangeDate')  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    photoid = models.ForeignKey('Photos', models.DO_NOTHING, db_column='PhotoId')  # Field name made lowercase.
    changeid = models.IntegerField(db_column='ChangeId', blank=True, null=True)  # Field name made lowercase.
    isaugmentation = models.BooleanField(db_column='IsAugmentation')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ChangePhotoRecords'


class Clients(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apitokenkey = models.TextField(db_column='ApiTokenKey', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    registraitionstatusid = models.IntegerField(db_column='RegistraitionStatusId')  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Clients'


class Datasetphotorecords(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    photoid = models.ForeignKey('Photos', models.DO_NOTHING, db_column='PhotoId')  # Field name made lowercase.
    datasetid = models.ForeignKey('Datasets', models.DO_NOTHING, db_column='DataSetId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSetPhotoRecords'


class Datasetphotos(models.Model):
    sideid = models.IntegerField(db_column='SideId')  # Field name made lowercase.
    skutodatasetid = models.ForeignKey('Skutodatasets', models.DO_NOTHING, db_column='SkuToDataSetId')  # Field name made lowercase.
    originalid = models.IntegerField(db_column='OriginalId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSetPhotos'


class Datasets(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    version = models.TextField(db_column='Version', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.TextField(db_column='Size', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    augmentedpercent = models.IntegerField(db_column='AugmentedPercent', blank=True, null=True)  # Field name made lowercase.
    zippath = models.TextField(db_column='ZipPath', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSets'


class Datasetsdates(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DataSetsDates'


class Designs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Designs'


class Equipments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    allowdivisions = models.BooleanField(db_column='AllowDivisions')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Equipments'


class Formfactortocategory(models.Model):
    categoriesid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoriesId')  # Field name made lowercase.
    formfactorsid = models.ForeignKey('Formfactors', models.DO_NOTHING, db_column='FormFactorsId')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    skucounter = models.IntegerField(db_column='SkuCounter')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FormFactorToCategory'


class Formfactors(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    size = models.TextField(db_column='Size', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    englishname = models.TextField(db_column='EnglishName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FormFactors'


class Ids(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Ids'


class Imagefromrecognizers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    pathurl = models.TextField(db_column='PathUrl', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    pricetagsversion = models.TextField(db_column='PriceTagsVersion', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shelftagsversion = models.TextField(db_column='ShelfTagsVersion', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    skudetectorversion = models.TextField(db_column='SkuDetectorVersion', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ImageFromRecognizers'


class Mlmodels(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    uploaddate = models.DateTimeField(db_column='UploadDate', blank=True, null=True)  # Field name made lowercase.
    isactual = models.BooleanField(db_column='IsActual', blank=True, null=True)  # Field name made lowercase.
    platformtype = models.IntegerField(db_column='PlatformType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MLModels'


class Manafacturer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manafacturer'


class Manufacturertocategory(models.Model):
    categoriesid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoriesId')  # Field name made lowercase.
    manafacturersid = models.ForeignKey(Manafacturer, models.DO_NOTHING, db_column='ManafacturersId')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    errorpercent = models.IntegerField(db_column='ErrorPercent', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    inwork = models.IntegerField(db_column='InWork', blank=True, null=True)  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.
    readyforlearn = models.IntegerField(db_column='ReadyForLearn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ManufacturerToCategory'


class Onetimepasswords(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=10, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    attempts = models.IntegerField(db_column='Attempts')  # Field name made lowercase.
    statusid = models.IntegerField(db_column='StatusId')  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    actionid = models.IntegerField(db_column='ActionId', blank=True, null=True)  # Field name made lowercase.
    newphone = models.TextField(db_column='NewPhone', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OneTimePasswords'


class Photos(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sideid = models.IntegerField(db_column='SideId')  # Field name made lowercase.
    skuid = models.ForeignKey('Sku', models.DO_NOTHING, db_column='SKUId')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreId', blank=True, null=True)  # Field name made lowercase.
    statusid = models.IntegerField(db_column='StatusId')  # Field name made lowercase.
    ischange = models.BooleanField(db_column='IsChange')  # Field name made lowercase.
    originalid = models.ForeignKey('self', models.DO_NOTHING, db_column='OriginalId', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    path = models.TextField(db_column='Path', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    processedbyphotouploader = models.BooleanField(db_column='ProcessedByPhotoUploader')  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    originalphoto = models.TextField(db_column='OriginalPhoto', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    selectioninterfaceitemid = models.IntegerField(db_column='SelectionInterfaceItemId', blank=True, null=True)  # Field name made lowercase.
    skutoscenariolinkid = models.IntegerField(db_column='SkuToScenarioLinkId', blank=True, null=True)  # Field name made lowercase.
    scenarioid = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='ScenarioId', blank=True, null=True)  # Field name made lowercase.
    scenariotype = models.IntegerField(db_column='ScenarioType', blank=True, null=True)  # Field name made lowercase.
    error = models.TextField(db_column='Error', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    superscenariosid = models.IntegerField(db_column='SuperScenariosId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Photos'


class Photosdates(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhotosDates'


class Sku(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shortname = models.TextField(db_column='ShortName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    brandid = models.ForeignKey(Brands, models.DO_NOTHING, db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    creatorid = models.ForeignKey('Users', models.DO_NOTHING, db_column='CreatorId', blank=True, null=True)  # Field name made lowercase.
    formfactorid = models.ForeignKey(Formfactors, models.DO_NOTHING, db_column='FormFactorId', blank=True, null=True)  # Field name made lowercase.
    barcode = models.TextField(db_column='Barcode', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # sizeid = models.ForeignKey('Sizes', models.DO_NOTHING, db_column='SizeId', blank=True, null=True)  # Field name made lowercase.
    # designid = models.ForeignKey(Designs, models.DO_NOTHING, db_column='DesignId', blank=True, null=True)  # Field name made lowercase.
    # volumeid = models.ForeignKey('Volumes', models.DO_NOTHING, db_column='VolumeId', blank=True, null=True)  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # manafacturer = models.TextField(db_column='Manafacturer', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # englishname = models.TextField(db_column='EnglishName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # manafacturerid = models.ForeignKey(Manafacturer, models.DO_NOTHING, db_column='ManafacturerId', blank=True, null=True)  # Field name made lowercase.
    # adoptedphotoscount = models.IntegerField(db_column='AdoptedPhotosCount')  # Field name made lowercase.
    # changedphotoscount = models.IntegerField(db_column='ChangedPhotosCount')  # Field name made lowercase.
    # unverifiedphotoscount = models.IntegerField(db_column='UnverifiedPhotosCount')  # Field name made lowercase.
    # rejectedphotoscount = models.IntegerField(db_column='RejectedPhotosCount')  # Field name made lowercase.
    # threshold = models.FloatField(db_column='Threshold', blank=True, null=True)  # Field name made lowercase.
    photolink = models.TextField(db_column='PhotoLink', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # statusid = models.IntegerField(db_column='StatusId')  # Field name made lowercase.
    # readystatusid = models.IntegerField(db_column='ReadyStatusId')  # Field name made lowercase.
    # test = models.IntegerField(blank=True, null=True)
    # createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    # sourcetype = models.IntegerField(db_column='SourceType', blank=True, null=True)  # Field name made lowercase.
    # updatedid = models.IntegerField(db_column='UpdatedId', blank=True, null=True)  # Field name made lowercase.
    # updatedate = models.DateTimeField(db_column='UpdateDate', blank=True, null=True)  # Field name made lowercase.
    # supercategoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='SuperCategoryId', blank=True, null=True)  # Field name made lowercase.
    # subcategoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='SubCategoryId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SKU'


class Scenarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    formfactorid = models.ForeignKey(Formfactors, models.DO_NOTHING, db_column='FormFactorId', blank=True, null=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    goal = models.IntegerField(db_column='Goal', blank=True, null=True)  # Field name made lowercase.
    imagepath = models.TextField(db_column='ImagePath', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    points = models.IntegerField(db_column='Points', blank=True, null=True)  # Field name made lowercase.
    time = models.IntegerField(db_column='Time', blank=True, null=True)  # Field name made lowercase.
    straight = models.IntegerField(db_column='Straight', blank=True, null=True)  # Field name made lowercase.
    fromtop = models.IntegerField(db_column='FromTop', blank=True, null=True)  # Field name made lowercase.
    fromleft = models.IntegerField(db_column='FromLeft', blank=True, null=True)  # Field name made lowercase.
    fromright = models.IntegerField(db_column='FromRight', blank=True, null=True)  # Field name made lowercase.
    frombottom = models.IntegerField(db_column='FromBottom', blank=True, null=True)  # Field name made lowercase.
    accepted = models.IntegerField(db_column='Accepted', blank=True, null=True)  # Field name made lowercase.
    needscheck = models.IntegerField(db_column='NeedsCheck', blank=True, null=True)  # Field name made lowercase.
    declined = models.IntegerField(db_column='Declined', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.IntegerField(db_column='SourceType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Scenarios'


class Selectedskus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    selectedids = models.TextField(db_column='SelectedIds', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SelectedSkus'


class Selectioninterfaceitems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    skuid = models.ForeignKey(Sku, models.DO_NOTHING, db_column='SkuId')  # Field name made lowercase.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreId', blank=True, null=True)  # Field name made lowercase.
    sideid = models.IntegerField(db_column='SideId')  # Field name made lowercase.
    adoptedphotoscount = models.IntegerField(db_column='AdoptedPhotosCount')  # Field name made lowercase.
    changedphotoscount = models.IntegerField(db_column='ChangedPhotosCount')  # Field name made lowercase.
    unverifiedphotoscount = models.IntegerField(db_column='UnverifiedPhotosCount')  # Field name made lowercase.
    rejectedphotoscount = models.IntegerField(db_column='RejectedPhotosCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SelectionInterfaceItems'


class Sizes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    width = models.TextField(db_column='Width', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    height = models.TextField(db_column='Height', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    depth = models.TextField(db_column='Depth', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sizes'


class Skutodatasets(models.Model):
    skuid = models.ForeignKey(Sku, models.DO_NOTHING, db_column='SkuId')  # Field name made lowercase.
    datasetid = models.ForeignKey(Datasets, models.DO_NOTHING, db_column='DataSetId')  # Field name made lowercase.
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SkuToDataSets'


class Skutoscenario(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    scenariosid = models.ForeignKey(Scenarios, models.DO_NOTHING, db_column='ScenariosId')  # Field name made lowercase.
    skusid = models.ForeignKey(Sku, models.DO_NOTHING, db_column='SkusId')  # Field name made lowercase.
    accepted = models.IntegerField(db_column='Accepted', blank=True, null=True)  # Field name made lowercase.
    needscheck = models.IntegerField(db_column='NeedsCheck', blank=True, null=True)  # Field name made lowercase.
    declined = models.IntegerField(db_column='Declined', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SkuToScenario'


class Statistic(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    skuquantity = models.IntegerField(db_column='SkuQuantity', blank=True, null=True)  # Field name made lowercase.
    formfactorsquantity = models.IntegerField(db_column='FormFactorsQuantity', blank=True, null=True)  # Field name made lowercase.
    scenariosquantity = models.IntegerField(db_column='ScenariosQuantity', blank=True, null=True)  # Field name made lowercase.
    pointsquantity = models.IntegerField(db_column='PointsQuantity', blank=True, null=True)  # Field name made lowercase.
    timequantity = models.IntegerField(db_column='TimeQuantity', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total', blank=True, null=True)  # Field name made lowercase.
    inwork = models.IntegerField(db_column='InWork', blank=True, null=True)  # Field name made lowercase.
    completed = models.IntegerField(db_column='Completed', blank=True, null=True)  # Field name made lowercase.
    readyforlearn = models.IntegerField(db_column='ReadyForLearn', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Statistic'


class Stores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stores'


class Superscenarios(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    # name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sourcetype = models.IntegerField(db_column='SourceType', blank=True, null=True)  # Field name made lowercase.
    goal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SuperScenarios'


class Users(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    login = models.TextField(db_column='Login', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleId')  # Field name made lowercase.
    isblocked = models.BooleanField(db_column='IsBlocked')  # Field name made lowercase.
    registrationdate = models.DateTimeField(db_column='RegistrationDate')  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    middlename = models.TextField(db_column='MiddleName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey(Stores, models.DO_NOTHING, db_column='StoreId', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apitokenkey = models.TextField(db_column='ApiTokenKey', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    photolink = models.TextField(db_column='PhotoLink', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Volumes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Volumes'


class Wrongrecognizers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    correctskuid = models.ForeignKey(Sku, models.DO_NOTHING, db_column='CorrectSkuId', blank=True, null=True)  # Field name made lowercase.
    correctimageurl = models.TextField(db_column='CorrectImageUrl', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WrongRecognizers'
