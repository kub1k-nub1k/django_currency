from rest_framework import serializers

from currency.models import Rate, Source, ContactUs
from django.conf import settings
from django.core.mail import send_mail


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sell',
            'created',
            'source',
            'currency_type',
        )


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Source
        fields = (
            'name',
            'code_name',
        )


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'email_from', 'subject', 'message']

    def create(self, validated_data):
        contact_us = super(ContactUsSerializer, self).create(validated_data)

        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
                Email: {contact_us.email_from}
                Subject: {contact_us.subject}
                Body: {contact_us.message}
                '''

        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False,
        )

        return contact_us
