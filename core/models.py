from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django_countries.fields import CountryField


class User(AbstractUser):
    # AbstractUser: username, password, first_name, last_name, email, date_joined, last_login
    def __str__(self) -> str:
        return self.username
  

class Molecular(models.Model):
    formula = models.CharField(max_length=100)
    structure = models.CharField(max_length=50, blank=True, null=True)
    other_info = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.formula

    def get_save_to_list_url(self):
        return reverse("core:save-to-list", kwargs={
            'formula': self.formula
        })
