from django.shortcuts import render,HttpResponse
from .models import Post,Categorias

# Create your views here.


def blog(request):
    categorias=Categorias.objects.all()
    blog=Post.objects.all() 
    return render(request,'blog/blog.html', {"blog":blog,"categorias":categorias})

def categoria(request,categorias_id):
    categoria=Categorias.objects.get(id=categorias_id)
    blog=Post.objects.filter(categorias=categoria)
    return render(request,'blog/categorias.html',{"categorias":categoria,"blog":blog})

