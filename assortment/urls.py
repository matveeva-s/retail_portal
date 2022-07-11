from django.urls import path

import assortment.views as views

app_name = 'assortment'

urlpatterns = [
    path('contract_matrix_options/', views.contract_matrix_options, name='contract_matrix_options'),
    path('retailers/list/', views.RetailersOptions.as_view(), name='retailers_options'),
    path('store_types/list/', views.StoreTypesOptions.as_view(), name='store_types_options'),
    path('regions/list/', views.RegionsOptions.as_view(), name='regions_options'),
    path('stores/list/', views.StoresOptions.as_view(), name='stores_options'),
    path('recommended_matrix/', views.RecommendedContactMatrix.as_view(), name='recommended_matrix'),
    path('contract_matrix/list/', views.ContractMatrixList.as_view(), name='contract_matrix_list'),
    path('contract_matrix/create/', views.ContractMatrixCreateAPI.as_view(), name='contract_matrix_create'),
]
