import re
from django.shortcuts import render, redirect

from blogproject.blogapp.forms import BlogForm
from .models import Blog
from django.utils import timezone

def home(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
        else:
            form = BlogForm()

        return render(request, 'form_create.html', {'form':form})
