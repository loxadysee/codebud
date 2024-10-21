from django.db import models

<<<<<<< HEAD
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True) # save the time when the record is updated 
    created_at = models.DateTimeField(auto_now_add=True) # save the time when the record is created
    
    def __str__(self):
        return self.name
=======
# Create your models here.test test hih test again

>>>>>>> 5212ec57dbe86aa42727d6ad5f794457450b0de7
