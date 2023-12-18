from django.shortcuts import render
from django.http import JsonResponse
from .models import Service, TypeService


def home(request):
    return render(request, "app/home.html")


def about_us(request):
    return render(request, "app/about_us.html")


def service(request):
    return render(request, "app/service.html")


def api_services(request):
    data = {
        'items': list(Service.objects.values())
    }
    return JsonResponse(data)
