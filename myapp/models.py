from django.db import models
from django.utils import timezone


class Value(models.Model):
    drinker = models.CharField(max_length = 100)
    add_date = models.DateTimeField(default=timezone.now)
    drinks_num = models.IntegerField(default = 0, max_length = 5)


    def __str__(self):
        return self.drinker



# Create your models here.
