
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

# from .views import home
from .views import (create_product,
                    delete_product, update_product,
                    ProductCreateView,
                    product_detail, products_list, Hell)


app_name = "products"

# domain.com/products
urlpatterns = [
    # path("", products_list, name="list-product"),
    path("", products_list, name="list-product"),
    path("create/", create_product, name="create-product"),
    # path("create/", ProductCreateView.as_view(), name="create-product"),
    path("delete/<int:pro_id>/", delete_product, name="delete-product"),
    path("update/<int:pro_id>/", update_product, name="update-product"),
    path("<slug:product_slug>/", product_detail, name="detail-product"),
    path("test/hi", Hell.as_view(), name="test")
    # path("test/", TemplateView.as_view(template_name="test.html"), name="test")

]
