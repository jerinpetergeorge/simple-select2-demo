from django.contrib import admin
from simple_select2 import Select2Admin, AutoCompleteSelect2Multiple, AutoCompleteSelect2
from .models import Reporter, Article, Publication


class ArticleAdmin(Select2Admin, admin.ModelAdmin):
    extra = {
        'publications': AutoCompleteSelect2Multiple(url='select2-publication-list'),
        'reporter': AutoCompleteSelect2(url='select2-reporter-list')
    }
    list_display = ('id', 'headline', 'reporter', 'pub_date')
    list_display_links = ('headline',)


admin.site.register(Reporter)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Publication)
