from currency.utils import generate_password as gp

from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, Http404
from currency.models import Rate

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