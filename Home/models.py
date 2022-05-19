from django.db import models

# Create your models here.
#Models are schemas for the collections in our database

#With each model that we create, we are basically creating a table with certain fields
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
        #Changes the entry name of the database 
