from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model): #this model should be registered in admin.py
    name = models.CharField(max_length=220)
    date = models.DateTimeField(auto_now_add=True) #store creation date

    def __str__(self):
        return str(self.name)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField(blank=True)
    """blank=True means this field is no longer required, this way we can use the save() method to calculate it"""
    salesman = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price= self.price * self.quantity
        super().save(*args, **kwargs) #reffering to the parent class

        def __str__(self):
            return "Sold {} - {} for {}".format(self.product.name, self.quantity, self.price, self.total_price)