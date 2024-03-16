from django.db import models

class URL(models.Model):
    url = models.URLField(unique = True)
    short_url = models.CharField(max_length=100, unique = True)