from django.contrib import admin
from .models import Waybill

class WaybillAdmin(admin.ModelAdmin):
    list_display = ('tracking_number',)
    search_fields = ('tracking_number',)
admin.site.register(Waybill, WaybillAdmin)