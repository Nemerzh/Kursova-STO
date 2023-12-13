from django.db import models


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    organization_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_num = models.IntegerField()

    class Meta:
        db_table = 'client'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AutoPart(models.Model):
    auto_part_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'auto_part'

    def __str__(self):
        return self.name


class TypeService(models.Model):
    type_service_id = models.AutoField(primary_key=True)
    name_service = models.CharField(max_length=255)

    class Meta:
        db_table = 'type_service'

    def __str__(self):
        return self.name_service


class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    time_of_work = models.IntegerField()
    type_service = models.ForeignKey(TypeService, on_delete=models.CASCADE)
    price = models.IntegerField()
    parts = models.ManyToManyField(AutoPart, through="ServiceAutoPart")

    class Meta:
        db_table = 'service'

    def __str__(self):
        return self.name


class ServiceAutoPart(models.Model):
    service_auto_part_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    auto_part = models.ForeignKey(AutoPart, on_delete=models.CASCADE)

    class Meta:
        db_table = 'service_auto_part'

    def __str__(self):
        return f"Service Auto Part {self.service_auto_part_id}"


class Contract(models.Model):
    contract_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    current_account = models.CharField(max_length=255, null=True, blank=True)
    duration = models.IntegerField()
    services = models.ManyToManyField(Service, through="ContractService")

    class Meta:
        db_table = 'contract'

    def __str__(self):
        return f"Contract {self.contract_id} for {self.client}"


class ContractService(models.Model):
    contract_service_id = models.AutoField(primary_key=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    price = models.IntegerField()

    class Meta:
        db_table = 'contract_service'

    def __str__(self):
        return f"Contract Service {self.contract_service_id}"
