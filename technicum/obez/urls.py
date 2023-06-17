from django.urls import path

from obez import views

app_name = 'obez'

urlpatterns = [
    path('', views.obez, name='obez'),
    path('obez_get_data/', views.obez_get_data, name='obez_get_data'),
]