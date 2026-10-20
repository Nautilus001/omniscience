from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return  self.name
    
class Container(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    # last_sync = models.DateTimeField(default=)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='containers')

    def __str__(self):
        return self.name
