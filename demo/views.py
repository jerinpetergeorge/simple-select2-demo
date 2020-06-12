from simple_select2 import AutoCompleteBaseView
from django.views import generic
from .models import Reporter, Publication, Article
from .forms import Select2ArticleModelForm


class ReporterView(AutoCompleteBaseView):
    model = Reporter
    search_fields = ('full_name', 'email')


class PublicationView(AutoCompleteBaseView):
    model = Publication
    search_fields = ('name',)


class ArticleCreateSelect2View(generic.CreateView):
    model = Article
    form_class = Select2ArticleModelForm
    template_name = 'demo/article_create.html'
