from core.abstract.models import AbstractModel
from django.db import models


# Create your models here.
class Book(AbstractModel):
    ISBN = models.CharField(max_length=20)
    title = models.CharField(max_length=500)
    release_year = models.IntegerField(default=0)
    publisher = models.CharField(max_length=500, default='Unknown')
    thumbnail = models.URLField()
    ratings = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    author = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        """This code is specifying that the database table for the model should be named."""
        db_table = "'core.book'"
