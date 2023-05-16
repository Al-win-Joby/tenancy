from django.contrib import admin

# Register your models here.
from sweet_tenant.models import Sweet

@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display =('name',)