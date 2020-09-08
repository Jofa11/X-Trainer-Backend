from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
