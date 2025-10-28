from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post




def home(request):
    
    context = {
        'cont': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'posts/home.html'
    context_object_name = 'cont'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'posts/about.html', {'title': 'About'})
