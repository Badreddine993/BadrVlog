from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import BlogPost


def index(request):
    blog_posts = BlogPost.objects.all()  # This should fetch all blog posts
    return render(request, 'index.html', {'blog_posts': blog_posts})

def about(request):
    return render(request, 'blog/about.html')

def post(request):
    return render(request, 'blog/post.html')

def contact(request):
    return render(request, 'blog/contact.html')

def article(request):
    return render(request, 'articles/article.html')

# views.py




def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_post_detail.html', {'post': post})