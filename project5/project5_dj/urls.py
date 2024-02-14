"""
URL configuration for project5_dj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from woe import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.admin, name='admin'),
    path('dev/', views.dev_page, name='dev_page'),
    path('user/', views.user_page, name='user_page'),

    path('do_manual_ingest', views.do_manual_ingest, name='do_manual_ingest'),
    path('user', views.user_request, name='user_request'),
    path('user-chart', views.user_request_chart, name='user_request_chard'),
    path('table_data', views.table_data, name="table_data"),

    path('django_admin/', admin.site.urls),
]
