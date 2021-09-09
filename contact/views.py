from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.mail import send_mail


# Create your views here.


def contactform(request):
    if request.method == 'POST':
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

# send an email

        send_mail(
            'Message from ' + message_name,  # subject
            message,  # message
            message_email,  # from email
            ['paceposters1@gmail.com'],  # to email
            )
        return render(request, 'contact/contactform.html', {'message_name': message_name})
    else:
        return render(request, 'contact/contactform.html')
