from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.CharField(max_length=150)
    text=models.CharField(max_length=500)
    date=models.DateTimeField()

    def __str__(self):
        return self.title