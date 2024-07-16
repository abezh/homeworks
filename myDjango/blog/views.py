from django.shortcuts import render, HttpResponse
from .models import Post
from requests import request


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, "base.html", {'posts': posts})
