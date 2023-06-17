from django.urls import path

from rexpl import views

app_name = 'rexpl'

urlpatterns = [
    path('', views.rexpl, name='rexpl'),
    path('rexpl_get_data/', views.rexpl_get_data, name='rexpl_get_data'),
]