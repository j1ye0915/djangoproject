from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'MainApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('menu',views.menu,name='menu'),
    path('menu/<int:pizza_id>/',views.pizzas,name='pizzas'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
