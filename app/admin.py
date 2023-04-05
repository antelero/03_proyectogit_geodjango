from django.contrib import admin
from django.contrib.gis import admin
from .models import Myplaces


admin.site.register(Myplaces, admin.ModelAdmin)