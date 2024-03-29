from django import forms

from currency.models import Source, Rate, ContactUs


class SourceForm(forms.ModelForm):

    class Meta:
        model = Source
        fields = (
            'name',
            'code_name',
            'logo_source',
        )


class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = (
            'buy',
            'sell',
            'currency_type',
            'source',
        )


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = (
            'email_from',
            'subject',
            'message',
        )
