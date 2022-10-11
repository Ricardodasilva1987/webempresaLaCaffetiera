from django.urls import path
from .views import *


urlpatterns = [
 
    #Path del pages
   
   
    path('<int:page_id>/', pages , name='pages'),#int cambia a un numero entero y se puede utilizar para filtrar, ya que si no le se pone se genera una cadena de caracteres
    
]