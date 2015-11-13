from django.db import models


class Book(models.Model):
    name = models.CharField(max_length="100")
    title = models.CharField(max_length="100", null=True, blank=True)
    content = models.CharField(max_length="100", null=True, blank=True)
