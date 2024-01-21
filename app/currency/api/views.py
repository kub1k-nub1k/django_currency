from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from currency.api.paginators import RatePagination, ContactUSPagination
from currency.api.serializers import RateSerializer, SourceSerializer, ContactUsSerializer
# from currency.api.throtling import RateThrottle
from currency.filters import RateFilter
from currency.models import Rate, Source, ContactUs


class RateViewSet(ModelViewSet):
    queryset = Rate.objects.all().order_by('-created')
    serializer_class = RateSerializer
    pagination_class = RatePagination
    filterset_class = RateFilter
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    ordering_fields = ('buy', 'sell', 'created')
    # throttle_classes = (RateThrottle,)


class SourceViewSet(ModelViewSet):
    queryset = Source.objects.all().order_by('-id')
    serializer_class = SourceSerializer


class ContactUsViewSet(ModelViewSet):
    queryset = ContactUs.objects.all().order_by('-id')
    serializer_class = ContactUsSerializer
    pagination_class = ContactUSPagination
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        filters.SearchFilter,
    )
    search_fields = ['email_from', 'subject', 'message']
