from django.contrib import admin
from cross_site import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Tag)
admin.site.register(models.Product)
