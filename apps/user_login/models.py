from __future__ import unicode_literals
from django.db import models

class dojo(models.Model):
    name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=2)

class ninjas(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    dojo = models.ForeignKey(dojo, on_delete=True, related_name="ninjas")
