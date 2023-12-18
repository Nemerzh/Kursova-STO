from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about_us', views.about_us, name="about"),
    path('service', views.service, name="service"),
    path('api/services', views.api_services, name="api_services")
]
