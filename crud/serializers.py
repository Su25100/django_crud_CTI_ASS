from rest_framework import serializers
from .models import Book_details


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
          model=Book_details
          fields = ('Book_name','Book_id')