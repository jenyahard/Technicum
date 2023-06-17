from django.urls import path

from tu import views

app_name = 'tu'

urlpatterns = [
    path('', views.tu, name='tu'),
    path('tu_get_data/', views.tu_get_data, name='tu_get_data'),
]