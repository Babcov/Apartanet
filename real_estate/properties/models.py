from django.db import models

# Create your models here.
from django.db import models

class Property(models.Model):
       title = models.CharField(max_length=255)
       description = models.TextField()
       price = models.DecimalField(max_digits=10, decimal_places=2)
       bedrooms = models.IntegerField()
       bathrooms = models.DecimalField(max_digits=4, decimal_places=2)
       # Добавьте остальные поля модели