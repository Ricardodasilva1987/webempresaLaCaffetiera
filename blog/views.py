from django.shortcuts import render,get_object_or_404
from .models import Post,Category

# Create your views here.

def blog(request):
    posts =Post.objects.all()
    return render(request,'blog/blog.html',{'posts':posts})


def category (request, category_id):
    #category = Category.objects.get(id=category_id)
    category= get_object_or_404(Category,id =category_id) #se usa este metodo que es un get si trae algo de la base o sino genera el error 404
    #posts = Post.objects.filter(categories=category)
    
    return render(request,'blog/category.html',{'category':category})