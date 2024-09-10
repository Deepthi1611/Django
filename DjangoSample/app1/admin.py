from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiCertificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    # list_display is a tuple
    list_display = ('name', 'type', 'date_added')
    inlines = [ChaiReviewInline]
    # inlines: This is an attribute used in Django's ModelAdmin class to specify related models that should be displayed inline (i.e., within the same form) when editing or adding an instance of the main model.

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('ChaiVarieties',)
    # filter_horizontal: This is an admin-specific setting that provides a better interface for managing many-to-many relationships. 
    # By default, Django admin displays many-to-many relationships with a dual listbox interface (i.e., a pair of select boxes where you move items from one to another).
    # Using filter_horizontal changes this to a widget with a horizontal filter, which makes it easier to select and manage related objects.

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'number')

# register the model in DB
admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)