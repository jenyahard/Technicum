from django.urls import path

from dul import views

app_name = 'dul'

urlpatterns = [
    path('', views.dul, name='dul'),
    path('dul_get_data/', views.dul_get_data, name='dul_get_data'),
]