from django.urls import path

from contract import views

app_name = 'contract'

urlpatterns = [
    path('', views.contract, name='contract'),
    path('contract_get_data/', views.contract_get_data, name='contract_get_data'),
]