from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product

def index(request):
    tovar = Product.objects.all()
    return render(request, "index.html", {"tovar":tovar})

def create(request):
    if request.method == "POST":
        tov = Product()
        tov.name = request.POST.get("name")
        tov.manufacturer = request.POST.get("manufacturer")
        tov.save()
    return HttpResponseRedirect("/")