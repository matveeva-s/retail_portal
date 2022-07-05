from datetime import timedelta

from django.db.models import Q
from django.utils import timezone
from recognizer_api.models import Storetypes, Regions, Storenetworks, Visits
from assortment.models import RecommendedAssortment, RecommendedMatrix
from scan_and_train.models import Sku
from recognizer_api.helpers import round_with_precision


def get_visits(retailer, region, store_type):
    week_ago = timezone.now() - timedelta(days=14)
    return Visits.objects.using('recognizer').filter(
        completiondate__lte=week_ago,
        storeid__storenetworkid=retailer,
        storeid__cityid__regionid=region,
        storeid__storetypeid=store_type,
    ).distinct()


def get_scus(visits):
    barcodes = visits.filter(
        visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode__isnull=True
    ).values_list(
        'visitequipments__visitbays__visitshelves__visitshelfproducts__barcode', flat=True
    )
    correct_barcodes = visits.filter(
        visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode__isnull=False,
    ).values_list(
        'visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode', flat=True
    )
    all_barcodes = list(set((list(barcodes) + list(correct_barcodes))))
    return Sku.objects.using('scan_and_train').filter(barcode__in=all_barcodes, name__isnull=False)


def get_product_visits(product, visits):
    return visits.filter(
        Q(
            visitequipments__visitbays__visitshelves__visitshelfproducts__barcode=product.barcode,
            visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode__isnull=True,
        ) |
        Q(visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode=product.barcode)
    ).distinct()


def get_distribution(product, visits):
    qset = get_product_visits(product, visits)
    return round_with_precision(qset.count() / visits.count())


def get_facing_amount(product, visits):
    qset = get_product_visits(product, visits)
    qset_facings = qset.values_list('visitequipments__visitbays__visitshelves__visitshelfproducts', flat=True)
    facings = 0
    if qset_facings.exists():
        facings = (qset_facings.count()) / (qset.count())
    return round_with_precision(facings)


def run():
    print('start')
    store_types = Storetypes.objects.using('recognizer').all()
    regions = Regions.objects.using('recognizer').all()
    retailers = Storenetworks.objects.using('recognizer').all()
    print('store_types:', store_types.count())
    print('regions:', regions.count())
    print('retailers:', store_types.count())
    print('summary iterations:', store_types.count() * regions.count() * store_types.count())
    print('---------')
    counter = 0

    for retailer in retailers:
        for store_type in store_types:
            for region in regions:
                counter += 1
                if counter > 3897:
                    visits = get_visits(retailer, region, store_type)
                    matrix = RecommendedMatrix.objects.create(
                        store_type=store_type.id,
                        retailer=retailer.id,
                        region=region.id,
                    )
                    if visits.exists():
                        products = get_scus(visits)
                        assortment = []
                        for product in products:
                            dist = get_distribution(product, visits)
                            facing = get_facing_amount(product, visits)
                            assortment_item = RecommendedAssortment(
                                matrix=matrix,
                                barcode=product.barcode,
                                scu=product.id,
                                distribution=dist,
                                facing_amount=facing,
                            )
                            assortment.append(assortment_item)
                        RecommendedAssortment.objects.bulk_create(assortment)
                        print(f'№{counter}:', retailer.id, store_type.id, region.id, products.count())
