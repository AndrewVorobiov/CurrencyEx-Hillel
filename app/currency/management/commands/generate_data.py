from django.core.management.base import BaseCommand, CommandError
from currency.models import Rate
from currency.models import ContactUs
import random
class Command(BaseCommand):
    help = 'Generate random records'

    def handle(self, *args, **options):
        for index in range(100):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=random.uniform(20, 30),
                buy=random.uniform(20, 30),
                source=random.choice(('privatbank''monobank', 'vKurse'))
            )
class Command(BaseCommand):