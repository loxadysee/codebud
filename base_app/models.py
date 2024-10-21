from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True) # save the time when the record is updated 
    created_at = models.DateTimeField(auto_now_add=True) # save the time when the record is created
    
    def __str__(self):
        return self.name