from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=200 , null=False, unique = True)
    storage_type = models.CharField(max_length=10 , null=False)

    def __str__(self):
        return self.name

