from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def youtube(request):
    return render(request, 'youtube.html')