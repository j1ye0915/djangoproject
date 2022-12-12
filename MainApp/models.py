from django.db import models
from django.db.models import Model
# Create your models here.

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=20)

    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'toppings'

    def __str__(self):
        return self.topping_name


class Image(Model):
    pizzaimg = models.ImageField(upload_to='photos',default='pizza.jpg')

