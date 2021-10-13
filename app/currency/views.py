from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from django.shortcuts import render

from currency.tasks import send_email_in_background

from currency.models import Rate, ContactUs
from currency.forms import RateForm, ContactUsForm


def index(request):
    return render(request, 'index.html')


class RateListView(ListView):
    template_name = 'rate_list.html'
    queryset = Rate.objects.all()


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


    def form_valid(self, form):
        data = form.cleaned_data
        body = f'''
        From: {data['email_from']}
        Topic: {data['subject']}
        
        Message:
        {data['message']}
        '''

       # send_email_in_background.delay(body)

        #from .tasks import print_hello_world
        #print_hello_world.delay()

        return super().form_valid(form)



