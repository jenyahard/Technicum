from django.urls import path

from smk import views

app_name = 'smk'

urlpatterns = [
    path('', views.smk, name='smk'),
    path('smk/', views.smk_get_data, name='smk'),
]