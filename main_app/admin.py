from django.contrib import admin

#import your models
from .models import Car, Maint

# Register your models here.
admin.site.register(Car)
admin.site.register(Maint)
