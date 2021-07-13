from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponseRedirect
from products.models import Product
from django.urls import reverse_lazy

# List View


def home(request):
    # response = HttpResponse()
    # response.content = "How are you"
    # response.headers["age"] = 25

    # return response

    # print(request.user.is_authenticated)

    products = Product.objects.all()

    # for product in products:
    #     print(product)

    # print(request.path)

    context = {
        "title": "How are you",
        "products": products
    }

    return render(request, "index.html", context)


# Create View
def create_product(request):
    if request.method == "GET":
        return render(request, "create-product.html")

    print(request.POST)
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

    print(reverse_lazy("products:list-product"))

    return HttpResponseRedirect(reverse_lazy("products:list-product"))
