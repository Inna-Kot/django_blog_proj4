from django.shortcuts import render

# Create your views here.
def my_blog(request):
    return render(request, 'blog/home.html')

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_superuser(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'YourStrongPassword123')
        return HttpResponse("Superuser created!")
    return HttpResponse("Superuser already exists!")
