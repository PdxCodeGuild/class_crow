from django.db import models

# Create your models here.

class Shortener(models.Model):
    shortened_url = models.CharField(max_length=255, blank=True, null=True)
    random_string_database = models.CharField(max_length=255, blank=True, null=True)
    count = models.IntegerField(default = 0)
    

    def __str__(self):
        return self.shortened_url