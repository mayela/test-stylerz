from django.contrib import admin

from dates.models import Date

class DateAdmin(admin.ModelAdmin):
    model = Date
    readonly_fields= ('end_datetime',)

admin.site.register(Date, DateAdmin)
