from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.


def home(request):
    #contact form database
    # if request.method == 'POST':
    #     name == request.POST['name']
    #     email == request.POST['email']
    #     subject == request.POST['subject']
    #     message == request.POST['message']
    #     contact = models.Home(name=name, email=email, subject=subject, message=message)
    #     contact.save()
    return render(request, 'index.html')


def project(request):
    return render(request, 'project.html')


def contact(request):
    context = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = "From: "+ email + "\n" 
        message += "Sender Name: "+ name + "\n\r\n\r" 
        message += "-------------------------------------------------------"
        message += "\n\r\n\r"

        message += request.POST['message']

        try:
            send_mail(
                'sample-mail - '+ name,# subject,
                message,#message
                email,# from email
                ['sonalimemane2020@gmail.com','sonali.pandhare93@gmail.com'],# to email,
                #fail_silently=False
            )
            context = {'mail_response':True}
        except Exception as err:
            raise err

    return render(request, 'index.html', context)


