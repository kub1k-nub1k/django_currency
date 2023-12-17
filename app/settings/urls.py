from django.contrib import admin
from django.urls import path, include

from currency.views import IndexView, change_password


urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('account.urls')),
    path('change-password/', change_password, name='change_password'),
    path('currency/', include('currency.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='index'),
]
