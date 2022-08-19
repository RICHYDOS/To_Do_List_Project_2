from distutils.sysconfig import customize_compiler
from email.quoprimime import body_check
import imp
from django.db import models
from django.conf import settings
from django.urls import reverse

class Item(models.Model):
    title = models.CharField(max_length=140)
    description = models.TextField(default="", blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("item_detail", kwargs={"pk": self.pk})
    