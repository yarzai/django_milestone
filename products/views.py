from django.http import HttpResponse
from django.shortcuts import redirect, render
from products.models import Product

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
