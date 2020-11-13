from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.

class Shortener(models.Model):
    shortened_url = models.CharField(max_length=255, blank=True, null=True)
    random_string_database = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(default = 0)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.shortened_url