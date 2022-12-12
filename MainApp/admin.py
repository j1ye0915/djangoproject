from django.contrib import admin
from .models import Pizza,Topping,Image

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Image)