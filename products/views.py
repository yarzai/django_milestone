from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from products.models import Product
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.base import TemplateView

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.base import View
from django.views.generic.list import ListView



def home(request):
    return HttpResponseRedirect(reverse_lazy("products:list-product"))

# List View


def products_list(request):
    products = Product.objects.all()
    context = {
        "title": "How are you",
        "products": products
    }
    return render(request, "products/list-products.html", context)

class ProductListView(ListView):
    model = Product
    template_name = 'products/list-products.html'
    context_object_name = "products"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "I am fine"
    #     return context
    


class Test(TemplateView):
    template_name = "test.html"
    extra_context = {"title": "How are you"}
    

# Create View
def create_product(request):
    if request.method == "GET":
        return render(request, "products/create-product.html")

    name = request.POST.get("name")
    price = request.POST.get("price")
    code = request.POST.get("code")
    quantity = request.POST.get("quantity")
    is_availible = request.POST.get("is_availible", "off")

    if is_availible == "on":
        is_availible = True
    else:
        is_availible = False

    product = Product.objects.create(name=name, price=price, code=code,
                                     quantity=quantity, is_availible=is_availible)
    product.save()

    return HttpResponseRedirect(reverse_lazy("products:list-product"))

# Delete View


def delete_product(request, pro_id):
    product = Product.objects.get(id=pro_id, name="Hp")
    product.delete()
    return HttpResponseRedirect(reverse_lazy("products:list-product"))


def update_product(request, pro_id):
    product = Product.objects.get(id=pro_id)
    # products = Product.objects.filter(id=pro_id)

    # products.update(name="dfds", code=15)
    if request.method == "GET":
        return render(request, "products/update-product.html", {"product": product})

    product.name = request.POST.get("name")
    product.price = request.POST.get("price")
    product.code = request.POST.get("code")
    product.quantity = request.POST.get("quantity")
    if request.POST.get("is_availible"):
        product.is_availible = True
    else:
        product.is_availible = False

    product.save()
    return HttpResponseRedirect(reverse_lazy("products:list-product"))
