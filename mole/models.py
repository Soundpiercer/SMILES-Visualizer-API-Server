from django.db import models


class Molecular(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    formula = models.CharField(max_length=100, blank=True, default="")
    effect = models.CharField(max_length=500, blank=True, default="")
    others = models.CharField(max_length=500, blank=True, default="")

    class Meta:
        ordering = ["created"]
