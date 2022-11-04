from django.contrib import admin
from .models import WildfireReport


class WildfireReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'town', 'reported_by', 'contact_number']


admin.site.register(WildfireReport, WildfireReportAdmin)