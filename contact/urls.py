from django.urls import path
from .views import *


urlpatterns = [

    # Path del contact

    path('', contacto, name='contact'),
    path('enviado/', contacto, name='enviado'),


]
