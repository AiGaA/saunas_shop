from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    stove_type = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_stove_type(self):
        return self.stove_type


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name