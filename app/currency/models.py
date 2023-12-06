from django.db import models
from currency.choices import CurrencyTypeChoices


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency_type = models.SmallIntegerField(
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD
    )
    source = models.CharField(max_length=255)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Source(models.Model):
    source_url = models.CharField(max_length=255)
    name = models.CharField(max_length=64)


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    time = models.IntegerField()
