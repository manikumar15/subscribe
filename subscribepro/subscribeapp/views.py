from django.shortcuts import render
from .models import News

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives



# Create your views here.

def newsletter2(request):
    email=request.POST.get('a1')
    f=News(Email=email)
    f.save()
    subject, from_email,recipient_list = 'IT Update', 'settings.EMAIL_HOST_USER',[f.Email]
    text_content = 'This is an important message.'
    html_content = '<h3><p>Thank you for Subscribing 😃 ... you will get notifications as soon as possible 😃 </p></h3>'
    msg = EmailMultiAlternatives(subject, text_content, from_email,recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request,'email.html')