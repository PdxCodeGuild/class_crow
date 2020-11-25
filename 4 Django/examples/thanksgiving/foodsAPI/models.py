from django.db import models
from users.models import CustomUser

class Food(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    name = models.CharField(max_length=60)
    rating = models.IntegerField(choices=Rating.choices)
    bringer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.name

