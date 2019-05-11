from django.shortcuts import render
from core.models import AboutSection

# Create your views here.
def index (request):
    about = AboutSection.objects.all()
    return render(request, 'index.html', {
        "about": about,
    })

def blog (request):
    return render(request, 'blog.html')

def blogpost (request):
    return render(request, 'blogpage.html')


def contact (request):
    return render(request, 'contact.html')
       