from django.db import models

# Create your models here.
class GoodMorning(models.Model):
    morning_text = models.CharField(max_length=200)

class GoodEvening(models.Model):
    evening_test = models.CharField(max_length=200)