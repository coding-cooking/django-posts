from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
def posts_list(request):
    articles = Post.objects.all().order_by("-date")
    return render(request, 'posts/posts_list.html', {"posts" : articles} )

def post_page(request, slug):
    article = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {"post" : article} )

#when post new post, it will check whether login, or will redirect to the login page
@login_required(login_url="/users/login/")
def post_new(request):
    return render(request, 'posts/post_new.html')