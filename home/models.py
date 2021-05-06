from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name        
    #this is to display the actual name of the person in admin page type srt for short after def


    # makemigrations means create changes and store it in a file
    # migrate means apply the pending change created by make migrations