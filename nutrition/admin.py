from django.contrib import admin

# Register your models here.

from .models import MainCategory, BasicStats, BasicFood, AllFood

admin.site.register(MainCategory)
admin.site.register(BasicStats)
admin.site.register(BasicFood)
admin.site.register(AllFood)