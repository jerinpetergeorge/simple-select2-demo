from django.urls import path
from .views import ReporterView, PublicationView

urlpatterns = [
    path('reporter/', ReporterView.as_view(), name='select2-reporter-list'),
    path('publication/', PublicationView.as_view(), name='select2-publication-list'),
]
