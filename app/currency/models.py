from django.db import models
from currency.choices import CurrencyTypeChoices
from django.utils.translation import gettext_lazy as _


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    currency_type = models.SmallIntegerField(
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=255)
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Source(models.Model):
    name = models.CharField(_('Source'), max_length=64)
    logo_source = models.FileField(_('logo'), default=None, null=True, blank=True, upload_to='logo/')

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    def __str__(self):
        return self.name


class RequestResponseLog(models.Model):
    path = models.CharField(max_length=255)
    request_method = models.CharField(max_length=10)
    time = models.IntegerField()
