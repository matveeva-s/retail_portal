from django.urls import path

import recognizer_api.views as views

app_name = 'recognizer_api'

urlpatterns = [
    path('visits/', views.VisitsApi.as_view(), name='visits_api'),
    path('visits/<int:pk>/', views.VisitApi.as_view(), name='visits_api'),
    path('visits/<int:pk>/products/', views.VisitProductsApi.as_view(), name='visits_products_api'),
    path('contract_matrix_options/', views.contract_matrix_options, name='contract_matrix_options'),
    path('recommended_matrix/', views.RecommendedContactMatrix.as_view(), name='recommended_matrix'),
    path('test_auth/', views.TestClosedApi.as_view(), name='test_auth'),
]
