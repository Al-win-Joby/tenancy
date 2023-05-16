from django.contrib import admin

# Register your models here.
from sweet_shared.models import Sweettype

# @admin.register(Sweettype)
# class SweetTypeAdmin(admin.ModelAdmin):
#     list_display=('name',) 


admin.site.register(Sweettype)   