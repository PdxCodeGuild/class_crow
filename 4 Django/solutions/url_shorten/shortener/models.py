from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model

class Url(models.Model):
    url = models.CharField(max_length=200)
    url_hash = models.CharField(max_length=200)
    date_added = models.DateTimeField(default=datetime.now)
    clicks = models.IntegerField(default=0)
    repeat_addition = models.IntegerField(default=0)
    last_ip = models.CharField(default='', max_length=20)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.url_hash

