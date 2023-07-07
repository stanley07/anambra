from django.db import models

class Building(models.Model):
    owner_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    building_type = models.CharField(max_length=100)
    amount_value = models.DecimalField(max_digits=8, decimal_places=2)
    contact = models.CharField(max_length=100)
    ansidd_no = models.CharField(max_length=100)
    image = models.ImageField(upload_to='building/images/')

    def __str__(self):
        return self.owner_name
