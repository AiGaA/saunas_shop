from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    stove_type = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_stove_type(self):
        return self.stove_type


class Product(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    name = models.CharField(max_length=254)
    product_type = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)


class ProductWithFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    features = models.ManyToManyField(ProductFeature)
