from django.shortcuts import render
from blogapp.models import Post, Categoria


# Create your views here.
def blog(request):
        posts = Post.objects.all()
        return render(request,"blogapp/blog.html", {"posts": posts})

def categoria(request, categoria_id):
        varCategoria = Categoria.objects.get(id=categoria_id)
        posts = Post.objects.filter(categorias=varCategoria)
        return render(request, "blogapp/categoria.html",{'categoria':varCategoria,"posts": posts})  