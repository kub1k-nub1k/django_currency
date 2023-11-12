from django.shortcuts import render
from django.http.response import HttpResponse
from currency.models import Rate
from currency.models import ContactUs


def rate_list(request):

    result = []
    rates = Rate.objects.all()

    for rate in rates:
        result.append(
            f'ID: {rate.id}, buy: {rate.buy}, sell: {rate.sell}, type: {rate.type}, '
            f'sourse: {rate.source}, created: {rate.created} <br>'
        )

    return HttpResponse(str(result))


def contactus_list(request):

    result = []
    contact = ContactUs.objects.all()

    for con in contact:
        result.append(
            f'ID: {con.id}, subject:{con.subject}, message:{con.message}'
        )

    return HttpResponse(str(result))



