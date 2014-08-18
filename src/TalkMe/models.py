from django.db import models

# Create your models here.

class TalkMessage(models.Model):
    nick = models.CharField(max_length = 10)
    message = models.CharField(max_length = 255)
    create_at = models.DateTimeField()
    status = models.BooleanField()
    pos = models.CharField(max_length = 100,blank = True)
    lat =models.DecimalField(max_digits = 8, decimal_places = 5,blank = True)
    lon = models.DecimalField(max_digits = 8, decimal_places = 5,blank = True)