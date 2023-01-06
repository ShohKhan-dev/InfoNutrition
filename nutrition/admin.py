from django.contrib import admin

# Register your models here.

from .models import MainCategory, BasicStats, BasicFood, AllFood, UseInfo, UserRDA, UserLog, UserSDA

admin.site.register(MainCategory)
admin.site.register(BasicStats)
admin.site.register(BasicFood)
admin.site.register(AllFood)
admin.site.register(UseInfo)

admin.site.register(UserRDA)
admin.site.register(UserSDA)
admin.site.register(UserLog)