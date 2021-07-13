
from django.contrib import admin
from django.urls import path
# from .views import home
from .views import home, create_product


app_name = "products"

# domain.com/products
urlpatterns = [
    path("", home, name="list-product"),
    path("create/", create_product, name="create-product")
]
