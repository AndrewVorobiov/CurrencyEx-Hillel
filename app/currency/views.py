from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView


from currency.utils import generate_password as gp

from django.shortcuts import render, get_object_or_404, reverse, redirect

from django.http import HttpResponseRedirect
from currency.models import Rate, ContactUs
from currency.forms import RateForm, ContactUsForm
from django.core.mail import send_mail


from annoying.functions import get_object_or_None


def index(request):
    return render(request, 'index.html')

# return render(request, 'rate_list.html', context=context)
class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


# def rate_details(request, pk):
# try:
# rate = Rate.objects.get(pk=pk)
# except Rate.DoesNotExist:
#   raise Http404(f"Rate does not exist with id {pk}")

#   rate = get_object_or_404(Rate, pk=pk)

####eturn render(request, 'rate_details.html', context=context)
class RateDetailView(DetailView):
    template_name = 'rate_details.html'
    queryset = Rate.objects.all()


class RateUpdateView(UpdateView):
    queryset = Rate.objects.all()
    template_name = 'rate_update.html'
    success_url = reverse_lazy('currency:rate-list')
    form_class = RateForm


class RateCreateView(CreateView):
    queryset = Rate.objects.all()
    template_name = 'rate_create.html'
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    success_url = reverse_lazy('currency:rate-list')

class CreateContactUs(CreateView):
    form_class = ContactUsForm
    template_name = 'contactus_form.html'
    success_url = reverse_lazy('index')
    #model = ContactUs
    #fields = (
      #   'email_from',
      #  'subject',
       # 'message',
    #)

    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}
        
        Message:
        {data['message']}
        '''


        send_mail(
            'ContactUs from Client',
            body,
            'testappsmtp123@gmail.com',
            ['dazhbog0@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)




