from unittest.mock import MagicMock
from decimal import Decimal
from currency.choices import CurrencyTypeChoices
from currency.constants import PRIVATBANK_CODE_NAME
from currency.models import Rate, Source
from currency.tasks import parse_privatbank, parse_monobank


def test_parse_privatbank(mocker):
    initial_count = Rate.objects.count()

    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.80000", "sale": "41.80000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )

    parse_privatbank()

    assert Rate.objects.count() == initial_count + 2
    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5'


def test_parse_privatbank_prevent_duplicates(mocker):
    privatbank_data = [
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "40.80000", "sale": "41.80000"},
        {"ccy": "USD", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
        {"ccy": "PLN", "base_ccy": "UAH", "buy": "37.50000", "sale": "38.10000"},
    ]
    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: privatbank_data)
    )
    source = Source.objects.get(code_name=PRIVATBANK_CODE_NAME)
    Rate.objects.create(source=source, buy="40.80", sell="41.80", currency_type=CurrencyTypeChoices.EUR)
    Rate.objects.create(source=source, buy="37.50", sell="38.10", currency_type=CurrencyTypeChoices.USD)
    initial_count = Rate.objects.count()

    parse_privatbank()

    assert Rate.objects.count() == initial_count
    assert requests_get_mock.call_count == 1


def test_parse_monobank(mocker):
    monobank_data = [
        {"currencyCodeA": 840, "currencyCodeB": 980, "rateBuy": 40.80000, "rateSell": 41.80000},
        {"currencyCodeA": 978, "currencyCodeB": 980, "rateBuy": 37.50000, "rateSell": 38.10000},
        {"currencyCodeA": 980, "currencyCodeB": 840, "rateBuy": 0.025, "rateSell": 0.026},
    ]

    Source.objects.create(code_name='monobank', name='Monobank')

    requests_get_mock = mocker.patch(
        'requests.get',
        return_value=MagicMock(json=lambda: monobank_data)
    )
    to_2_places_decimal_mock = mocker.patch(
        'currency.tasks.to_2_places_decimal',
        side_effect=lambda x: Decimal(str(x))
    )

    initial_count = Rate.objects.count()

    parse_monobank()

    expected_created_rate_count = 2

    assert Rate.objects.count() == initial_count + expected_created_rate_count

    assert requests_get_mock.call_count == 1
    assert requests_get_mock.call_args[0][0] == 'https://api.monobank.ua/bank/currency'
    assert to_2_places_decimal_mock.call_count == expected_created_rate_count * 2
