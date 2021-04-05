from django.contrib.auth.models import User
from django.db import models


class SearchRequest(models.Model):
    # product = models.OneToOneField(Product, null=True, blank=True, on_delete=models.SET_NULL)
    text = models.CharField("request text", max_length=255)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, default=None)

