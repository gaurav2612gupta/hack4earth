from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from .models import Post
# Create your views here.



def post(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/posts.html', context)


def home(request):
    return render(request, 'blog/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'author']



def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
