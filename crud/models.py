from django.db import models

# Create your models here.
class Book_details(models.Model):
    Book_name=models.CharField(max_length=100)
    Book_id=models.CharField(max_length=10,primary_key=True)
   
    def __str__(self):
        return self.Book_name 