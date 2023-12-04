from django.contrib import admin
from currency.models import Source, ContactUs


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'source_url',
        'name'
    )


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'email_from',
        'subject',
        'message'
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
