from django.urls import path

from smk import views

app_name = 'smk'

urlpatterns = [
    path('', views.smk, name='smk'),
    path('smk_get_data/', views.smk_get_data, name='smk_get_data'),
]