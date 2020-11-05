from django.db import models
from datetime import datetime


# Create your models here.

class Item(models.Model):
    to_do_item = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField('date created', default=datetime.now, blank=True)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.to_do_item