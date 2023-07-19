from django.contrib import admin

# Register your models here.
from .models import SmallDogs
from .models import LargeDogs

admin.site.register(SmallDogs)
admin.site.register(LargeDogs)