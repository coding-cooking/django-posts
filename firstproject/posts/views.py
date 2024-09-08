from django.shortcuts import render
from .models import Post

# Create your views here.
def posts_list(request):
    articles = Post.objects.all().order_by("-date")
    return render(request, 'posts/posts_list.html', {"posts" : articles} )

def post_page(request, slug):
    article = Post.objects.get(slug=slug)
    return render(request, 'posts/posts_page.html', {"post" : article} )
