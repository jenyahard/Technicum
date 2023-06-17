from django.urls import path

from passport import views

app_name = 'passport'

urlpatterns = [
    path('', views.passport, name='passport'),
    path('passport_get_data/', views.passport_get_data, name='passport_get_data'),
]