from django.urls import path
from .views import *


urlpatterns = [

    # Path del core
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('store/', store, name='store'),



]
