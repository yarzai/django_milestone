from django.contrib import admin
from products.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "code",
                    "quantity", "is_availibe", "updated", "created"]


admin.site.register(Product, ProductAdmin)
