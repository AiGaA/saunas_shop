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


class StoveFeature(models.Model):
    name = models.CharField(max_length=254)
    stove_type = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_stove_type(self):
        return self.stove_type


class WindowFeature(models.Model):
    name = models.CharField(max_length=254)
    window_type = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_window_type(self):
        return self.window_type


class Product(models.Model):
    stove_feature = models.ForeignKey('StoveFeature', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    window_feature = models.ForeignKey('WindowFeature', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def total_price(self):
        return sum(self.price * self.stove_feature.price * self.window_feature.price)