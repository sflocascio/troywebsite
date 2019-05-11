from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from core.models import AboutSection

# Create your views here.
def index (request):
    about = AboutSection.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print("These are the form Fields: ")
        print(name,email, message)

        #Email ourselves the submitted contact message 

        subject = 'Contact Form Received'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.DEFAULT_TO_EMAIL]
        print("This is the to and from email: ")
        print(from_email, to_email)

        context = {
            'user': name, 
            'email': email, 
            'message': message
        }

        contact_message = get_template('contact_message.txt').render(context)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)

        return redirect('home')

    return render(request, 'index.html', {
        "about": about,
    })

def blog (request):
    return render(request, 'blog.html')

def blogpost (request):
    return render(request, 'blogpage.html')


def contact (request):
    return render(request, 'contact.html')
       