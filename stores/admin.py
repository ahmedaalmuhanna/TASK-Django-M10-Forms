from atexit import register
from django.contrib import admin
from stores import models

# Register your models here.
admin.site.register(models.StoreItem)