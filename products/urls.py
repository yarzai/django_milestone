
from django.contrib import admin
from django.urls import path
# from .views import home
from .views import products_list, create_product, delete_product, update_product


app_name = "products"

# domain.com/products
urlpatterns = [
    path("", products_list, name="list-product"),
    path("create/", create_product, name="create-product"),
    path("delete/<int:pro_id>/", delete_product, name="delete-product"),
    path("update/<int:pro_id>/", update_product, name="update-product")
]
