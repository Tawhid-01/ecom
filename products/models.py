from django.db import models
from base.models import BAseModel
from django.utils.text import slugify
# Create your models here.
class category(BAseModel):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='category/')
    slug = models.SlugField(unique=True,null=True,blank=True)

    # description = models.TextField()
    def __str__(self):
          return self.category_name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(category, self).save(*args, **kwargs)
          

      
        
class ColorVariant(BAseModel):
    color_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.color_name


class SizeVariant(BAseModel):
    size_name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.size_name
    

class Product(BAseModel):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE,related_name='products')
    price = models.IntegerField()
    slug = models.SlugField(unique=True,null=True,blank=True)
    product_description = models.TextField()
    color_variants = models.ManyToManyField(ColorVariant,related_name='color_variants',blank=True)
    size_variants = models.ManyToManyField(SizeVariant,related_name='size_variants',blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
          
    # These must be outside the save() method
    def __str__(self):
        return self.product_name
        
    def get_product_price_by_size(self, size):
        return self.price + SizeVariant.objects.get(size_name=size).price
    
    def get_product_price_by_color(self, color_name):
        variant = self.color_variants.filter(color_name=color_name).first()
        return self.price + (variant.price if variant else 0)


class ProductImage(BAseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='products/')


class Coupon(BAseModel):
    coupon_code = models.CharField(max_length=255)
    is_expired = models.BooleanField(default=False)
    discount = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=500)