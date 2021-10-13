from celery import shared_task
from django.core.mail import send_mail

import requests

@shared_task
def parse_privatbank():
    from currency.models import Rate

    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()

    available_currency_types = ('USD', 'EUR')
    source = 'privatbank'

    for curr in currencies:
        currency_type = curr['ccy']
        if currency_type in available_currency_types:
            from currency.utils import to_decimal
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, type=currency_type).order_by('created').last()
            if (
                    previous_rate is None or #rate does not exist, create the first one
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
            )
            else:
                print(f'Rate already exist: {sale} {buy}')



@shared_task
def send_email_in_background(body):
    send_mail(
        'ContactUs from Client',
        body,
        'testappsmtp123@gmail.com',
        ['dazhbog0@gmail.com'],
        fail_silently=False,
    )
