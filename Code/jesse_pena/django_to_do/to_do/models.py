from django.db import models


# Create your models here.

class Item(models.Model):
    to_do_item = models.CharField(max_length=50, blank=True, null=True)
    # created_date = models.DateTimeField('date created')
    # completed_item = 
    # completed_yes_no = 

    def __str__(self):
        return self.to_do_item