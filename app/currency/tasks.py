from celery import shared_task
import requests

from currency.constants import PRIVATBANK_CODE_NAME, MONOBANK_CODE_NAME
from currency.models import Rate, Source
from currency.choices import CurrencyTypeChoices
from currency.utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=PRIVATBANK_CODE_NAME, defaults={'name': 'PrivatBank'})

    rates = response.json()

    available_currency_types = {
        'USD': CurrencyTypeChoices.USD,
        'EUR': CurrencyTypeChoices.EUR
    }

    for rate in rates:
        buy = to_2_places_decimal(rate['buy'])
        sell = to_2_places_decimal(rate['sale'])
        currency_type = rate['ccy']

        if currency_type not in available_currency_types:
            continue

        currency_type = available_currency_types[currency_type]

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source
            )


@shared_task
def parse_monobank_task():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    response.raise_for_status()

    source, _ = Source.objects.get_or_create(code_name=MONOBANK_CODE_NAME, defaults={'name': 'Monobank'})

    available_currency_types = {
        840: CurrencyTypeChoices.USD,
        978: CurrencyTypeChoices.EUR
    }

    rates = response.json()

    for rate_data in rates:
        currency_code_a = rate_data['currencyCodeA']
        currency_code_b = rate_data['currencyCodeB']

        if (currency_code_a, currency_code_b) not in [(840, 980), (978, 980)]:
            continue

        buy = to_2_places_decimal(rate_data.get('rateBuy'))
        sell = to_2_places_decimal(rate_data.get('rateSell'))

        currency_type = available_currency_types.get(currency_code_a)

        if currency_type is None:
            continue

        last_rate = Rate.objects.filter(source=source, currency_type=currency_type).order_by('-created').first()

        if last_rate is None or last_rate.buy != buy or last_rate.sell != sell:
            Rate.objects.create(
                buy=buy,
                sell=sell,
                currency_type=currency_type,
                source=source
            )
