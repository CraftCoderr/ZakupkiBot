from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    searchRequest = models.OneToOneField(SearchRequest, null=True, blank=True, on_delete=models.SET_NULL)


class SearchRequest(models.Model):
    product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.SET_NULL)
