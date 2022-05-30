from django.shortcuts import render

# Create your views here.

def youtube(request):
    return render(request, "youtube.html")


def one(request):
    return render(request, "one.html")


def two(request):
    return render(request, "two.html")


def three(request):
    return render(request, "three.html")