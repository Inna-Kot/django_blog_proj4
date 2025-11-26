from django.shortcuts import render

# Create your views here.
def my_blog(request):
    return render(request, 'blog/home.html')
