from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def services(request):
    return render(request, 'pages/services.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['subject'] or 'Contact Form Submission',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['placeholder@email.com'],
            )
            return HttpResponseRedirect('pages/thanks.html')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

def thanks(request):
    return render(request, 'pages/thanks.html')
