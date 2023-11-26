from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from currency.forms import SourceForm
from .models import Rate, ContactUs, Source


def rate_list(request):
    rates = Rate.objects.all()
    context = {'rates': rates}
    return render(request, 'rate.html', context)


def contactus_list(request):
    contact_messages = ContactUs.objects.all()
    context = {'contactus': contact_messages}
    return render(request, 'contactus.html', context)


def source_list(request):
    sources = Source.objects.all()
    form = SourceForm()
    context = {
        'sources': sources,
        'form': form
    }

    return render(request, 'source_list.html', context)


def source_create(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')
    else:
        form = SourceForm()
    return render(request, 'source_create.html', {'form': form})


def source_update(request, pk):

    rate = get_object_or_404(Source, id=pk)

    if request.method == 'POST':
        form = SourceForm(request.POST, instance=rate)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source/list/')

    elif request.method == 'GET':
        form = SourceForm(instance=rate)

    context = {
        'form': form
    }

    return render(request, 'source_update.html', context)


def source_delete(request, pk):
    source = get_object_or_404(Source, pk=pk)
    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source/list/')
    return render(request, 'source_delete.html', {'source': source})


def source_details(request, pk):
    source = get_object_or_404(Source, id=pk)
    context = {'source': source}
    return render(request, 'source_details.html', context)
