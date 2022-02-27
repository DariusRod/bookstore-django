from django.shortcuts import render
from .models import Category,Product

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def home(request):
    query=Product.objects.all()
    return render(request,'home.html',{'query':query})
