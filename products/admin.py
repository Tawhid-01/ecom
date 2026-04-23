from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageAdmin
    ]
    list_display = ['product_name','category','price']

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    model = SizeVariant
    list_display = ['size_name','price']

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    model = ColorVariant
    list_display = ['color_name','price']

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductImage)
