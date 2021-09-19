from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render, HttpResponseRedirect, get_object_or_404
from products.models import Product, ProductModelManager
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic.base import TemplateView

from django.views.generic.base import TemplateResponseMixin
from django.views.generic.base import View
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from exercise.forms import ProductModalForm, TestForm
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.views.generic.base import ContextMixin

TEST = 5


def home(request):
    return HttpResponseRedirect(reverse_lazy("products:list-product"))

# List View


# @login_required(login_url='/admin/login/')
def products_list(request):
    # if request.user.is_authenticated:
    products = Product.objects.all().is_availible()

    print(products.count())
    context = {
        "title": "How are you",
        "products": products
    }
    return render(request, "products/list-products.html", context)

    # raise Http404

# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/list-products.html'
#     context_object_name = "products"
    # queryset = Product.objects.filter()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["title"] = "I am fine"
    #     return context


class TestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "test.html")


class CustomModelFormMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        print(context)
        return context


# @login_required(login_url='/admin/login/')
# @method_decorator(login_required(login_url='/admin/login/'), name='dispatch')
class Hell(ModelFormMixin, CustomModelFormMixin, TemplateView):
    template_name = "test.html"
    model = Product
    fields = '__all__'
    extra_context = {"title": "How are you"}

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     print("Test")
    #     return super().dispatch(*args, **kwargs)


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


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    template_name = "products/create.html"


# Delete View


def delete_product(request, pro_id):
    product = Product.objects.get(id=pro_id)
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

    # product.save()
    messages.success(request, "Product have been updated successfully.")
    messages.error(request, "Product have not been updated successfully.")
    return HttpResponseRedirect(reverse_lazy("products:list-product"))

# DetailView


def product_detail(request, product_slug):

    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        raise Http404
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=product_slug).first()

    # product = get_object_or_404(Product, slug=product_slug)

    return render(request, "products/product_detail.html", {"product": product})
