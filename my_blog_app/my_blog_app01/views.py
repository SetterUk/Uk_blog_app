from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.
# def home(request):
#     return render(request,'home.html' , {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'


class articleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    context_object_name = 'article'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'