from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Post, category
from .forms import PostForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request,'home.html' , {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date_posted']  # Order by ID in descending order


class articleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    context_object_name = 'article'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCategoryView(CreateView):
    model = category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    fields = ['title', 'title_tag', 'body']
    success_url = reverse_lazy('home')
