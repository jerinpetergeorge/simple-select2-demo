from django.urls import path
from .views import ReporterView, PublicationView, ArticleCreateSelect2View

urlpatterns = [
    path('reporter/', ReporterView.as_view(), name='select2-reporter-list'),
    path('publication/', PublicationView.as_view(), name='select2-publication-list'),
    path('article/create/', ArticleCreateSelect2View.as_view(), name='article-create-view')
]
