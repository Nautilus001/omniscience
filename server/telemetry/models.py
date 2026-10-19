from django.db import models

# Create your models here.
class Container(models.Model):
    name = models.CharField(200)
    image = models.CharField(200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(200)
    client = models.CharField(200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return  self.name