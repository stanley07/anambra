from django.db import models

class Building(models.Model):
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    building_type = models.CharField(max_length=100)
    number_flats = models.CharField(max_length=1000, blank=True, null=True)
    amount_value = models.DecimalField(max_digits=8, decimal_places=2)
    ansidd_no = models.CharField(max_length=100)
    geographical_zone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.DecimalField(max_digits=14, decimal_places=0, blank=True, null=True)
    agent_id = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='building/images/')

    def __str__(self):
        return self.owner_name
