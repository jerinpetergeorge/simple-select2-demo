from django.contrib import admin
from .models import Author, Article, Publication

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Publication)
