from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Desktop,Laptop,Mobiles)
class viewAdmin(admin.ModelAdmin):
	pass