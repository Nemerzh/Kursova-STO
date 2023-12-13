from django.contrib import admin
from .models import Client, AutoPart, TypeService, Service, ServiceAutoPart, Contract, ContractService


admin.site.register(Client)
admin.site.register(AutoPart)
admin.site.register(TypeService)
admin.site.register(Service)
admin.site.register(ServiceAutoPart)
admin.site.register(Contract)
admin.site.register(ContractService)
# Register your models here.
