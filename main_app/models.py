from django.db import models
from django.urls import reverse
from datetime import date

SERVICES = (
    ('W', 'Wash'),
    ('T', 'Tires'),
    ('O', 'Oil'),
)

# Create your models here.

class Part(models.Model):
  name = models.CharField(max_length=50)
  purpose = models.CharField(
        'Purpose(Interior or Exterior)',
        max_length=20,
    )


  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('parts_detail', kwargs={'pk': self.id})

class Car(models.Model):
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=300)
    parts = models.ManyToManyField(Part)

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id':self.id})

class Maint(models.Model):
    date = models.DateField('Date of Service')
    service = models.CharField(
        max_length=1,
        choices=SERVICES,
        default=SERVICES[0][0]
    )

    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_service_display()} on {self.date}"

    class Meta:
        ordering = ['-date']