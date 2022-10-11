from django.urls import path
from .views import blog, category


urlpatterns = [
 
    #Path del blog
   
    path('', blog , name='blog'),
    path('category/<int:category_id>/', category , name='category'),#int cambia a un numero entero y se puede utilizar para filtrar, ya que si no le se pone se genera una cadena de caracteres
    
]