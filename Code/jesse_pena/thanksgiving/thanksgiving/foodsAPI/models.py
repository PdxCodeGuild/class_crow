from django.db import models

# Create your models here.



class Food(models.Model):
    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    name = models.CharField(max_length=60)
    rating = models.IntegerField(choices = Rating.choices)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=60)
    for_food = models.ForeignKey(Food, on_delete=models.CASCADE, blank = True, null = True, related_name = 'Food')

    def __str__(self):
        return self.name

