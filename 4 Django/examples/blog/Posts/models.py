from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Joke(models.Model):
    category = models.TextField(max_length=15, default=None)
    punchline = models.TextField(max_length=200, default=None)

    def __str__(self):
        return self.punchline