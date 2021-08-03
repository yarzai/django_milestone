from django.contrib import admin
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


admin.site.register(Product, ProductAdmin)
