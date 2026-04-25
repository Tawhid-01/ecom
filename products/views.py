# from pydoc import render_doc
# from tkinter import E
from django.shortcuts import render,redirect
from products.models import Product



def get_product(req, slug):
    try:
        product = Product.objects.get(slug=slug)
        context = {'product': product}
        
        # Start with the base price of the product
        final_price = product.price 

        # Add size variant price if selected
        selected_size = req.GET.get('size')
        if selected_size:
            size_variant = product.size_variants.get(size_name=selected_size)
            final_price += size_variant.price
            context['selected_size'] = selected_size

        # Add color variant price if selected
        selected_color = req.GET.get('color')
        if selected_color:
            color_variant = product.color_variants.get(color_name=selected_color)
            final_price += color_variant.price
            context['selected_color'] = selected_color

        context['updated_price'] = final_price
        return render(req, 'product.html', context)

    except Exception as e:
        print(f"Error logic: {e}")
        return redirect('/')