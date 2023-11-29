from django.contrib import admin
from django.urls import path

from currency.views import rate_list
from currency.views import contactus_list
from currency.views import source_list
from currency.views import source_create
from currency.views import source_update
from currency.views import source_delete
from currency.views import source_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('contactus/list/', contactus_list),
    path('source/list/', source_list),
    path('source/create/', source_create),
    path('source/update/<int:pk>/', source_update),
    path('source/delete/<int:pk>/', source_delete),
    path('source/details/<int:pk>/', source_details),

]
