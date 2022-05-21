from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Baytostore(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    equipmenttostoreid = models.ForeignKey('Equipmenttostore', models.DO_NOTHING, db_column='EquipmentToStoreId')  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    deletetypeid = models.ForeignKey('Deletetype', models.DO_NOTHING, db_column='DeleteTypeId', blank=True, null=True)  # Field name made lowercase.
    photolink = models.TextField(db_column='PhotoLink', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    sortekey = models.IntegerField(db_column='SorteKey', blank=True, null=True)  # Field name made lowercase.
    visitbayid = models.ForeignKey('Visitbays', models.DO_NOTHING, db_column='VisitBayId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BayToStore'


class Boundboxes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1')  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2')  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1')  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2')  # Field name made lowercase.
    imagefromrecognizerid = models.ForeignKey('Imagefromrecognizers', models.DO_NOTHING, db_column='ImageFromRecognizerId', blank=True, null=True)  # Field name made lowercase.
    skuid = models.IntegerField(db_column='Skuid', blank=True, null=True)  # Field name made lowercase.
    ismain = models.BooleanField(db_column='IsMain')  # Field name made lowercase.
    cordx1 = models.IntegerField(db_column='CordX1')  # Field name made lowercase.
    cordx2 = models.IntegerField(db_column='CordX2')  # Field name made lowercase.
    cordy1 = models.IntegerField(db_column='CordY1')  # Field name made lowercase.
    cordy2 = models.IntegerField(db_column='CordY2')  # Field name made lowercase.
    productid = models.IntegerField(db_column='ProductId', blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    pricetagvalue = models.DecimalField(db_column='PriceTagValue', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BoundBoxes'


class Brands(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Brands'


# class Bugs(models.Model):
#     id = models.AutoField(db_column='Id')  # Field name made lowercase.
#     date = models.DateField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
#     image = models.TextField(db_column='Image', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#     sku = models.TextField(db_column='Sku', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'Bugs'


class Categories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    parentid = models.ForeignKey('self', models.DO_NOTHING, db_column='ParentId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    englishname = models.TextField(db_column='EnglishName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Categories'


class Cities(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    regionid = models.ForeignKey('Regions', models.DO_NOTHING, db_column='RegionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cities'


class Deletetype(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sortekey = models.IntegerField(db_column='SorteKey', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DeleteType'


class Designs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Designs'


class Equipmenttostore(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Stores', models.DO_NOTHING, db_column='StoreId')  # Field name made lowercase.
    visitid = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitId')  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    photolink = models.TextField(db_column='PhotoLink', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    supercategoryid = models.IntegerField(db_column='SuperCategoryId', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    sortekey = models.IntegerField(db_column='SorteKey', blank=True, null=True)  # Field name made lowercase.
    equipmenttypeid = models.IntegerField(db_column='EquipmentTypeId')  # Field name made lowercase.
    visitequipmentid = models.ForeignKey('Visitequipments', models.DO_NOTHING, db_column='VisitEquipmentId')  # Field name made lowercase.
    allowdivision = models.BooleanField(db_column='AllowDivision')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EquipmentToStore'


class Federaldistricts(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FederalDistricts'


class Formfactors(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    size = models.TextField(db_column='Size', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    englishname = models.TextField(db_column='EnglishName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FormFactors'


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


class Mlcategorymodels(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    uploaddate = models.DateTimeField(db_column='UploadDate')  # Field name made lowercase.
    isactual = models.BooleanField(db_column='IsActual', blank=True, null=True)  # Field name made lowercase.
    platformtype = models.IntegerField(db_column='PlatformType')  # Field name made lowercase.
    verified = models.BooleanField(db_column='Verified')  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    classifieroutput = models.TextField(db_column='ClassifierOutput', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MLCategoryModels'


class Mlmodels(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type')  # Field name made lowercase.
    uploaddate = models.DateTimeField(db_column='UploadDate')  # Field name made lowercase.
    isactual = models.BooleanField(db_column='IsActual', blank=True, null=True)  # Field name made lowercase.
    platformtype = models.IntegerField(db_column='PlatformType')  # Field name made lowercase.
    verified = models.BooleanField(db_column='Verified')  # Field name made lowercase.
    approveddate = models.DateTimeField(db_column='ApprovedDate', blank=True, null=True)  # Field name made lowercase.
    size = models.IntegerField(db_column='Size', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='Version', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MLModels'


class Manufacturers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manufacturers'


class Products(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    skuid = models.TextField(db_column='SKUID', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shortname = models.TextField(db_column='ShortName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fatness = models.FloatField(db_column='Fatness', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    brand = models.TextField(db_column='Brand', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    manufacture = models.TextField(db_column='Manufacture', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate')  # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bigweigth = models.BooleanField(db_column='BigWeigth', blank=True, null=True)  # Field name made lowercase.
    depth = models.IntegerField(db_column='Depth', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Categories, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    brandid = models.ForeignKey(Brands, models.DO_NOTHING, db_column='BrandId', blank=True, null=True)  # Field name made lowercase.
    manufacturerid = models.IntegerField(db_column='ManufacturerId', blank=True, null=True)  # Field name made lowercase.
    formfactorid = models.ForeignKey(Formfactors, models.DO_NOTHING, db_column='FormFactorId', blank=True, null=True)  # Field name made lowercase.
    volumeid = models.ForeignKey('Volumes', models.DO_NOTHING, db_column='VolumeId', blank=True, null=True)  # Field name made lowercase.
    sizeid = models.ForeignKey('Sizes', models.DO_NOTHING, db_column='SizeId', blank=True, null=True)  # Field name made lowercase.
    designid = models.ForeignKey(Designs, models.DO_NOTHING, db_column='DesignId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Products'


class Regions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    federaldistrictid = models.ForeignKey(Federaldistricts, models.DO_NOTHING, db_column='FederalDistrictId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Regions'


class Sizes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    width = models.TextField(db_column='Width', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    height = models.TextField(db_column='Height', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    depth = models.TextField(db_column='Depth', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sizes'


class Storenetworks(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    generalpassforall = models.BooleanField(db_column='GeneralPassForAll')  # Field name made lowercase.
    logo = models.TextField(db_column='Logo', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreNetworks'


class Storetypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreTypes'


class Stores(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    storenetworkid = models.ForeignKey(Storenetworks, models.DO_NOTHING, db_column='StoreNetworkId')  # Field name made lowercase.
    cityid = models.ForeignKey(Cities, models.DO_NOTHING, db_column='CityId')  # Field name made lowercase.
    address = models.TextField(db_column='Address', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    contactinfo = models.TextField(db_column='ContactInfo', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nopass = models.BooleanField(db_column='NoPass')  # Field name made lowercase.
    generalpassforall = models.BooleanField(db_column='GeneralPassForAll')  # Field name made lowercase.
    # position = models.TextField(db_column='Position', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    directorname = models.TextField(db_column='DirectorName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    directorlastname = models.TextField(db_column='DirectorLastName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    directormiddlename = models.TextField(db_column='DirectorMiddleName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    equipmentscheme = models.TextField(db_column='EquipmentScheme', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    frontphoto = models.TextField(db_column='FrontPhoto', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    storetypeid = models.ForeignKey(Storetypes, models.DO_NOTHING, db_column='StoreTypeId', blank=True, null=True)  # Field name made lowercase.
    shortaddress = models.TextField(db_column='ShortAddress', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    haseanreader = models.BooleanField(db_column='HasEanReader')  # Field name made lowercase.
    lastvisitdate = models.DateTimeField(db_column='LastVisitDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Stores'


class Storestocategories(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    storeid = models.IntegerField(db_column='StoreId')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoresToCategories'


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
    phone = models.TextField(db_column='Phone', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apitokenkey = models.TextField(db_column='ApiTokenKey', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class Visitbayunrecognizeditems(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    bayid = models.ForeignKey('Visitbays', models.DO_NOTHING, db_column='BayId')  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1')  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2')  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1')  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2')  # Field name made lowercase.
    height = models.FloatField(db_column='Height')  # Field name made lowercase.
    width = models.FloatField(db_column='Width')  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitBayUnrecognizedItems'


class Visitbays(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    internalid = models.IntegerField(db_column='InternalId', blank=True, null=True)  # Field name made lowercase.
    photolink = models.TextField(db_column='PhotoLink', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visitequipmentid = models.ForeignKey('Visitequipments', models.DO_NOTHING, db_column='VisitEquipmentId')  # Field name made lowercase.
    photoname = models.TextField(db_column='PhotoName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    photoexternalid = models.TextField(db_column='PhotoExternalId', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    processedbyphotouploader = models.BooleanField(db_column='ProcessedByPhotoUploader')  # Field name made lowercase.
    processedbycroper = models.BooleanField(db_column='ProcessedByCroper')  # Field name made lowercase.
    errormasage = models.TextField(db_column='ErrorMasage', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitBays'


class Visitequipments(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    visitid = models.ForeignKey('Visits', models.DO_NOTHING, db_column='VisitId')  # Field name made lowercase.
    equipmenttypeid = models.IntegerField(db_column='EquipmentTypeId')  # Field name made lowercase.
    photolink = models.TextField(db_column='PhotoLink', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    photoname = models.TextField(db_column='PhotoName', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    photoexternalid = models.TextField(db_column='PhotoExternalId', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    processedbyphotouploader = models.BooleanField(db_column='ProcessedByPhotoUploader')  # Field name made lowercase.
    supercategoryid = models.IntegerField(db_column='SuperCategoryId', blank=True, null=True)  # Field name made lowercase.
    errormasage = models.TextField(db_column='ErrorMasage', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitEquipments'


class Visitshelfemptyspaces(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shelfid = models.ForeignKey('Visitshelves', models.DO_NOTHING, db_column='ShelfId')  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1')  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2')  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1')  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2')  # Field name made lowercase.
    height = models.FloatField(db_column='Height')  # Field name made lowercase.
    width = models.FloatField(db_column='Width', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitShelfEmptySpaces'


class Visitshelfpricetags(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    shelfid = models.ForeignKey('Visitshelves', models.DO_NOTHING, db_column='ShelfId')  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1')  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2')  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1')  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2')  # Field name made lowercase.
    height = models.FloatField(db_column='Height')  # Field name made lowercase.
    width = models.FloatField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    number = models.IntegerField(db_column='Number', blank=True, null=True)  # Field name made lowercase.
    confidence = models.FloatField(db_column='Confidence')  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitShelfPriceTags'


class Visitshelfproducts(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    ordernumber = models.IntegerField(db_column='OrderNumber', blank=True, null=True)  # Field name made lowercase.
    shelfid = models.ForeignKey('Visitshelves', models.DO_NOTHING, db_column='ShelfId')  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1')  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2')  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1')  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2')  # Field name made lowercase.
    height = models.FloatField(db_column='Height')  # Field name made lowercase.
    width = models.FloatField(db_column='Width', blank=True, null=True)  # Field name made lowercase.
    supercategoryid = models.IntegerField(db_column='SuperCategoryId', blank=True, null=True)  # Field name made lowercase.
    categoryproductclassifierversion = models.TextField(db_column='CategoryProductClassifierVersion', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    barcode = models.TextField(db_column='Barcode', db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    verificationstatus = models.BooleanField(db_column='VerificationStatus', blank=True, null=True)  # Field name made lowercase.
    pricetagnumber = models.IntegerField(db_column='PriceTagNumber', blank=True, null=True)  # Field name made lowercase.
    pricetagid = models.ForeignKey(Visitshelfpricetags, models.DO_NOTHING, db_column='PriceTagId', blank=True, null=True)  # Field name made lowercase.
    confidence = models.FloatField(db_column='Confidence')  # Field name made lowercase.
    correctbarcode = models.TextField(db_column='CorrectBarcode', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    processedbysntphotouploader = models.BooleanField(db_column='ProcessedBySnTPhotoUploader')  # Field name made lowercase.
    processedbycroper = models.BooleanField(db_column='ProcessedByCroper')  # Field name made lowercase.
    cropedphoto = models.TextField(db_column='CropedPhoto', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    errormasage = models.TextField(db_column='ErrorMasage', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitShelfProducts'


class Visitshelves(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    internalid = models.IntegerField(db_column='InternalId', blank=True, null=True)  # Field name made lowercase.
    bayid = models.ForeignKey(Visitbays, models.DO_NOTHING, db_column='BayId')  # Field name made lowercase.
    x1 = models.FloatField(db_column='X1', blank=True, null=True)  # Field name made lowercase.
    x2 = models.FloatField(db_column='X2', blank=True, null=True)  # Field name made lowercase.
    y1 = models.FloatField(db_column='Y1', blank=True, null=True)  # Field name made lowercase.
    y2 = models.FloatField(db_column='Y2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VisitShelves'


class Visits(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    storeid = models.ForeignKey(Stores, models.DO_NOTHING, db_column='StoreId')  # Field name made lowercase.
    completiondate = models.DateTimeField(db_column='CompletionDate')  # Field name made lowercase.
    skudetectorversion = models.IntegerField(db_column='SkuDetectorVersion')  # Field name made lowercase.
    pricetagsdetectorversion = models.IntegerField(db_column='PriceTagsDetectorVersion')  # Field name made lowercase.
    shelvesdetectorversion = models.IntegerField(db_column='ShelvesDetectorVersion')  # Field name made lowercase.
    categoryclassifierversion = models.IntegerField(db_column='CategoryClassifierVersion', blank=True, null=True)  # Field name made lowercase.
    skuclassifierversion = models.IntegerField(db_column='SkuClassifierVersion', blank=True, null=True)  # Field name made lowercase.
    unifiedclassifierversion = models.IntegerField(db_column='UnifiedClassifierVersion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Visits'


class Volumes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Volumes'
