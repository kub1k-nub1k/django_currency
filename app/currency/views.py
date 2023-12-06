from django.core.mail import send_mail
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy

from currency.forms import RateForm, SourceForm, ContactUsForm
from currency.models import Rate, Source, ContactUs


class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-create')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class RateDetailView(DetailView):
    model = Rate
    template_name = 'rate_detail.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-create')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'


class SourceDetailView(DetailView):
    model = Source
    template_name = 'source_detail.html'


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class ContactUsCreateView(CreateView):
    model = ContactUs
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    fields = (
        'email_from',
        'subject',
        'message',
    )

    def _send_email(self):
        from django.conf import settings
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
                Email: {self.object.email_from}
                Subject: {self.object.subject}
                Body: {self.object.message}
                '''

        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

        return redirect


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactUsForm
    success_url = reverse_lazy('currency:contactus-list')
    template_name = 'contactus_update.html'


class ContactUsDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('currency:contactus-list')
    template_name = 'contactus_delete.html'


class ContactUsDetailView(DetailView):
    model = ContactUs
    template_name = 'contactus_detail.html'


class IndexView(TemplateView):
    template_name = 'index.html'
