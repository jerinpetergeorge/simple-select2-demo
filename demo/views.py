from simple_select2 import AutoCompleteBaseView
from .models import Reporter, Publication


class ReporterView(AutoCompleteBaseView):
    model = Reporter
    search_fields = ('full_name', 'email')


class PublicationView(AutoCompleteBaseView):
    model = Publication
    search_fields = ('name',)
