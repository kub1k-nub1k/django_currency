# from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Rate, ContactUs


def rate_list(request):
    rates = Rate.objects.all()
    context = {'rates': rates}
    return render(request, 'rate.html', context)


def contactus_list(request):
    contact_messages = ContactUs.objects.all()
    context = {'contactus': contact_messages}
    return render(request, 'contactus.html', context)
