from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from products.models import Product
from django.urls import reverse_lazy
from django.db.models import Q


def home(request):
    return HttpResponseRedirect(reverse_lazy("products:list-product"))

# List View


def products_list(request):
    # response = HttpResponse()
    # response.content = "How are you"
    # response.headers["age"] = 25

    # return response

    # print(request.user.is_authenticated)

    products = Product.objects.filter(
        Q(is_availible=True) &
        Q(id=9) |
        Q(name="hp")
    )

    # for product in products:
    #     print(product)

    # print(request.path)

    context = {
        "title": "How are you",
        "products": products
    }

    return render(request, "products/list-products.html", context)


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
