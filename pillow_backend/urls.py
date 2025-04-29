"""
URL configuration for pillow_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('pillow/user/', views.UserList.as_view(), name='user_list'),
    path('pillow/user/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),
    path('pillow/listing/', views.ListingList.as_view(), name='listing_list'),
    path('pillow/listing/<int:pk>/', views.ListingDetail.as_view(), name='listing_detail'),
]


