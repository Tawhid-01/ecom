from django.db import models
from base.models import BAseModel
from django.utils.text import slugify
# Create your models here.
class category(BAseModel):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='category/')
    slug = models.SlugField(unique=True,null=True,blank=True)
    # description = models.TextField()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(category, self).save(*args, **kwargs)
          

        def __str__(self):
            return self.category_name

class Product(BAseModel):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(category, on_delete=models.CASCADE,related_name='products')
    price = models.IntegerField()
    slug = models.SlugField(unique=True,null=True,blank=True)
    product_description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)
          

        def __str__(self):
            return self.product_name



class ProductImage(BAseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_images')
    image = models.ImageField(upload_to='products/')

