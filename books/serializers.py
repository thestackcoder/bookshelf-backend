from rest_framework import serializers
from .models import Book
from authors.models import Author
from storages.models import Storage
from topics .models import Topic


class BookSerializer(serializers.ModelSerializer):
    book_photo = serializers.ImageField(required=False)
    author_firstname = serializers.CharField(source='author.first_name', read_only=True)
    author_lastname = serializers.CharField(source='author.last_name', read_only=True)
    topic_name = serializers.CharField(source='topic.name', read_only=True)
    storage_name = serializers.CharField(source='storage.name', read_only=True)
    class Meta:
        model = Book
        fields = ['id','title','book_photo','author','topic','storage','author_firstname','author_lastname','topic_name','storage_name']