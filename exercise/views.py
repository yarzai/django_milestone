from django.http.response import HttpResponse
from django.shortcuts import render
from exercise.forms import TestForm, ProductModalForm

# Create your views here.

def test(request):
    form = TestForm(data=request.POST or None, 
    initial={"text": "some text", "integer": "50", "boolean": True})
    if request.method == 'POST':
        if form.is_valid():
            print(form.cleaned_data.get('email'))
    
    return render(request, 'test.html',{"form": form})


def productForm(request):
    form = ProductModalForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            form.save()



    return render(request, 'test.html', {"form": form})