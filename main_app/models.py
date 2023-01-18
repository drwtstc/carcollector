from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.name