from rest_framework.serializers import ModelSerializer
from . models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "public_id",
            "ISBN",
            "release_year",
            "publisher",
            "thumbnail",
            "ratings",
            "price",
            "author",
            "created",
            "updated",
        ]