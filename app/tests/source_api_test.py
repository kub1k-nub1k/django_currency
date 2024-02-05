import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from currency.models import Source
from currency.api.serializers import SourceSerializer
from rest_framework.viewsets import ModelViewSet

pytestmark = pytest.mark.django_db


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all().order_by('-id')
    serializer_class = SourceSerializer
    basename = 'source'


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_source():
    return Source.objects.create(
        name='Test Source',
        code_name='test-source'
    )


def test_read_source(api_client, create_source):
    url = reverse('currency_api:source-detail', kwargs={'pk': create_source.id})
    response = api_client.get(url)
    assert response.status_code == 200


def test_create_source(api_client, create_source):
    url = reverse('currency_api:source-list')
    data = {
        'name': 'New Source',
        'code_name': 'new-source'
    }
    response = api_client.post(url, data)
    assert response.status_code == 201


def test_update_source(api_client, create_source):
    url = reverse('currency_api:source-detail', kwargs={'pk': create_source.id})
    data = {
        'name': 'Updated Source',
        'code_name': 'updated-source'
    }
    response = api_client.put(url, data)
    assert response.status_code == 200


def test_delete_source(api_client, create_source):
    url = reverse('currency_api:source-detail', kwargs={'pk': create_source.id})
    response = api_client.delete(url)
    assert response.status_code == 204
