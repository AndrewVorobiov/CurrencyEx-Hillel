from django.db import models


class Rate(models.Model):
    type = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)
class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    email_from = models.EmailField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()
class Bank(models.Model):
    name = models.CharField(max_length=25)
    url = models.CharField(max_length=60)


