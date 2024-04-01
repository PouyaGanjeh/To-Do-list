from django.db import models

# Create your models here.

class ToDo_Item (models.Model):
    ActivityName = models.CharField(max_length = 300)