"""technicum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from main_page.views import login_view, logout_view, about_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('main_page.urls', namespace='main_page')),
    path('passport/', include('passport.urls', namespace='passport')),
    path('tu/', include('tu.urls', namespace='tu')),
    path('rexpl/', include('rexpl.urls', namespace='rexpl')),
    path('contract/', include('contract.urls', namespace='contract')),
    path('smk/', include('smk.urls', namespace='smk')),
    path('obez/', include('obez.urls', namespace='obez')),
    path('dul/', include('dul.urls', namespace='dul')),
    path('about/', about_view, name='about'),
    path('logout/', logout_view, name='logout'),
    path('', login_view, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
