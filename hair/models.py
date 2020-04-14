from django.db import models
from datetime  import datetime
from django.utils import timezone
# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Time = models.DateTimeField(default=timezone.now)
    Service = models.CharField(max_length=100)
    Description = models.TextField(max_length=500)

    def __str__(self):
        return self.Name
