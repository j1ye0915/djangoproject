from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request, 'MainApp/index.html')

def menu(request):
    menu = Pizza.objects.all()
    context = {'all_menu':menu}
    return render(request, 'MainApp/menu.html', context)

def pizzas(request,pizza_id):
    p = Pizza.objects.get(id=pizza_id)

    toppings = Topping.objects.filter(pizza=p)

    context = {'pizza':p,'toppings':toppings}

    return render(request, 'MainApp/pizzas.html', context)

def uploadInfo(request):
    if request.method == 'POST':
        # img = request.FILES.get('photo')
        # user = request.FILES.get('photo').name
        new_img = models.Avatar(
            photo=request.FILES.get('photo'),
            user=request.FILES.get('photo').name 
        )
        new_img.save()
 
    return render(request, 'upload.html')