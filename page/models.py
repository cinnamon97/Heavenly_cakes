from django.db import models

# Create your models here.

class Contactus(models.Model):
    firstname=models.CharField(max_length=150)
    email=models.EmailField()
    topic=models.CharField(max_length=150)
    message=models.TextField()

    def __str__(self):
        return self.firstname