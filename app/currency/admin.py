from django.contrib import admin
from currency.models import Rate



from import_export import resources
from import_export.admin import ImportExportModelAdmin
class RateResource(resources.ModelResource):

    class Meta:
        model = Rate

class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
    list_display = (
        'id',
        'buy',
        'sale',
        'type',
        'source',
        'created',
    )
    list_filter = (
        'type',
        'source',


    )
    search_fields = (
        'type',
        'source',
    )
    readonly_fields = (
        'buy',
        'sale',
    )
    #def has_delete_permission(self, request, obj=None):
     #   return False
admin.site.register(Rate, RateAdmin)
