from rest_framework import routers

from currency.api.views import RateViewSet, SourceViewSet,  ContactUsViewSet

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'rates', RateViewSet, basename='rate')
router.register(r'sources', SourceViewSet, basename='source')
router.register(r'contactus', ContactUsViewSet, basename='contactus')

app_name = 'currency_api'

urlpatterns = [
    # path('rates/', RateListAPIView.as_view(), name='rate-list'),
    # path('rates/<int:pk>/', RateDetailsAPIView.as_view(), name='rate-details'),
] + router.urls
