from django.shortcuts import render
from products.models import Product

# Create your views here.

def index(req):

    context = {'products' : Product.objects.all()}
    return render(req , 'index.html', context)