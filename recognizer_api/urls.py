from django.urls import path

import recognizer_api.views as views

app_name = 'recognizer_api'

urlpatterns = [
    path('visits/', views.VisitsApi.as_view(), name='visits_api'),
    path('visits/test_visit/', views.test_visit_json, name='test_visit'),
    path('visits/<int:pk>/', views.VisitApi.as_view(), name='visits_api'),
]
