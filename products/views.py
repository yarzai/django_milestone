from django.http import HttpResponse
from django.shortcuts import redirect, render


def home(request):
    # response = HttpResponse()
    # response.content = "How are you"
    # response.headers["age"] = 25

    # return response

    # print(request.user.is_authenticated)
    print(request.path)

    context = {
        "title": "How are you"
    }

    return render(request, "index.html", context)
