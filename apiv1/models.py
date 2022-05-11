from django.db import models

# Create your models here.
class Works(models.Model):
    Worksname = models.CharField(max_length=100)
    Timelimit = models.DateField()