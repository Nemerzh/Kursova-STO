from .models import Client, AutoPart, TypeService, Service, ServiceAutoPart, Contract, ContractService
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class MyAdminSite(admin.AdminSite):
    site_header = 'Станція ТО'
    site_title = "СТО"
    # Інші налаштування адміністративного інтерфейсу, якщо потрібно


# Реєстрація вашого зміненого адміністративного сайту
admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin.site = admin_site

admin.site.register(Client)
admin.site.register(AutoPart)
admin.site.register(TypeService)
admin.site.register(Service)
admin.site.register(ServiceAutoPart)
admin.site.register(Contract)
admin.site.register(ContractService)
# Register your models here.
