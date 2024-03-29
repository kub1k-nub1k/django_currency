from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from currency.views import IndexView, change_password


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('account.urls')),
    path('change-password/', change_password, name='change_password'),
    path('currency/', include('currency.urls')),

    path('api/account/', include('account.api.urls')),
    path('api/currency/', include('currency.api.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
