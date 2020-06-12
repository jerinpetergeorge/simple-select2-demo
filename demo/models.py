from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Reporter(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.full_name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    publications = models.ManyToManyField(Publication, blank=True)
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
