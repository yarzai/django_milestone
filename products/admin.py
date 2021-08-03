from django.contrib import admin
from django.utils.timesince import timesince
from products.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "code",
                    "quantity", "is_availible", "updated", "created"]
    list_filter = ["price", "is_availible", "name"]
    search_fields = ["price", "name", "code"]
    list_per_page = 2
    list_editable = ["is_availible", "code"]
    # save_as_continue = False

    
    fields = ["name", "price", "code",
                    "quantity", "is_availible","updated", "created", "added_on" ]
    readonly_fields = ["updated", "created", "added_on"]

    # def added_on(self, instance, *args, **kwargs):
    #     return instance.added_on



admin.site.register(Product, ProductAdmin)
