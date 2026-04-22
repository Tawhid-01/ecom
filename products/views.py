from pydoc import render_doc
from tkinter import E
from django.shortcuts import render,redirect
from products.models import Product




def get_product(request , slug):
    # try:
        # product = Product.objects.get(slug =slug)
        return render(request  , 'product.html' )

    # except Exception as e:
    #     print(e)
       