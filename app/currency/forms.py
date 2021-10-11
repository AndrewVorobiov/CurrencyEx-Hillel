from django import forms
from currency.models import Rate, ContactUs

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = (
            'type',
            'sale',
            'buy',
            'source',
        )
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
        'email_from',
        'subject',
        'message'
        )

