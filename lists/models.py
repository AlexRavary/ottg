from django.db import models


# Create your models here.
class Item(models.Model):
    text = models.TextField(default='')

# ToDo: Adjust model so that items are associated with different lists
