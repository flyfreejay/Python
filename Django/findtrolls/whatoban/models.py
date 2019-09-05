from django.db import models

class Summoner(models.Model):
    name = models.CharField(max_length=16)
    
