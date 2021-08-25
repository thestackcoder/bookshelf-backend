from django.db import models
from authors.models import Author 
from topics.models import Topic
from storages.models import Storage

class Book(models.Model):
    title = models.CharField(max_length=200 , null=False, unique = True)
    book_photo = models.ImageField(upload_to='image/',blank=True)
    author = models.ForeignKey(Author, related_name="author",on_delete= models.PROTECT)
    topic = models.ForeignKey(Topic, related_name="topic",on_delete= models.PROTECT)
    storage = models.ForeignKey(Storage,related_name="storage",on_delete= models.PROTECT)


    def __str__(self):
        return self.title
