from django.db import models

class Empresa(models.Model):
    nit= models.IntegerField(primary_key=True,unique=True)
    name= models.CharField(max_length=40, unique=True)
    address= models.CharField(max_length=100, blank=True)
    telephone= models.IntegerField(blank=True)

    def __str__(self):
        return self.name