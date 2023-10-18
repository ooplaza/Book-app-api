from .models import Book
from django.contrib import admin


# Register your models here.
@admin.register(Book)
class CustomBookAdmin(admin.ModelAdmin):
    list_display = [
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
