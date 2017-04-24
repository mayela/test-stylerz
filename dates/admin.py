from django.contrib import admin

from dates.models import Date, DateHidden

class DateAdmin(admin.ModelAdmin):
    model = Date
    readonly_fields= ('end_datetime',)

    def get_queryset(self, request):
        qs = super(DateAdmin, self).get_queryset(request)
        qs = qs.filter(hide=False)
        return qs


class DateHiddenAdmin(admin.ModelAdmin):
    model = DateHidden
    readonly_fields= (
            'treatment_type', 
            'customer', 
            'specialist', 
            'start_datetime', 
            'end_datetime', 
            'hide'
            )

    def get_queryset(self, request):
        qs = super(DateHiddenAdmin, self).get_queryset(request)
        qs = qs.filter(hide=True)
        return qs

admin.site.register(Date, DateAdmin)
admin.site.register(DateHidden, DateHiddenAdmin)
