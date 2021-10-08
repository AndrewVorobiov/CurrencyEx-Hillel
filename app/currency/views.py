from currency.utils import generate_password as gp

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404, HttpResponseRedirect
from currency.models import Rate
from currency.forms import RateForm

from annoying.functions import get_object_or_None

def generate_password(request):
    password = gp()
    return HttpResponse(password)
def rate_list(request):
    queryset = Rate.objects.all()
    #print(queryset.count())
    ids= []
    for rate in queryset:
        ids.append(rate.id)

    context = {
        'objects': queryset,

        }


    return render(request, 'rate_list.html', context=context)
def rate_details(request, pk):
    #try:
       # rate = Rate.objects.get(pk=pk)
    #except Rate.DoesNotExist:
     #   raise Http404(f"Rate does not exist with id {pk}")

    rate = get_object_or_404(Rate, pk=pk)

    context = {
        'object': rate,
    }
    return render(request, 'rate_details.html', context=context)


def rate_create(request):


    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')

    else:
        form = RateForm()

    context = {
        'message': 'Rate Create',
        'form': form,
        'count': Rate.objects.count(),
    }

    return render(request, 'rate_create.html', context=context)

def rate_update(request, pk):
    instance = get_object_or_404(Rate, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        form = RateForm(form_data, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/currency/rate/list/')

    elif request.method == 'GET':
                form = RateForm(instance=instance)

    context = {
              'form': form,
          }
    return render(request, 'rate_update.html', context=context)
def rate_delete(request, pk):
    instance = get_object_or_None(Rate, pk=pk)
    instance.delete()
    return HttpResponseRedirect('/currency/rate/list/')
