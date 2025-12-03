from django.shortcuts import render

# Create your views here.
def my_blog(request):
    return render(request, 'blog/home.html')

from django.contrib.auth.models import User
from django.http import HttpResponse

