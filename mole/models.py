from django.db import models


class Molecular(models.Model):
    owner = models.ForeignKey(
        "auth.User", related_name="molecular", on_delete=models.CASCADE, null=False
    )
    created = models.DateTimeField(auto_now_add=True)
    formula = models.CharField(max_length=100, blank=True, default="")
    effect = models.CharField(max_length=500, blank=True, default="")
    others = models.CharField(max_length=500, blank=True, default="")

    class Meta:
        ordering = ["created"]
