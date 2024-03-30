from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ProductFeature(models.Model):
    name = models.CharField(max_length=254)
    price_increment = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    productfeatures = models.ManyToManyField(ProductFeature, blank=True)

    def __str__(self):
        return self.name


class ProductWithFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    features = models.ManyToManyField(ProductFeature)
