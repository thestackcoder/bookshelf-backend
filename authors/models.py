from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200 , null=False)
    last_name = models.CharField(max_length=500 , null=False)
    auther_photo = models.ImageField(upload_to='auther_image/',blank=True)

    def __str__(self):
        return self.first_name
