import pandas as pd
from django.db import transaction
from core.book.models import Book


def run():
    """
    Bulk Create Books.
    Return bulk of books
    To run this code, python manage.py runscript create_book.
    """
    datasets = pd.read_csv("./Datasets/Books.csv", low_memory=False)
    with transaction.atomic():
        bulk_books = [
            Book(
                ISBN=ISBN,
                title=TITLE,
                release_year=RELEASE_YEAR,
                publisher=PUBLISHER,
                thumbnail=THUMBNAIL,
                ratings=RATINGS,
                price=PRICE,
                author=AUTHOR,
            )
            for ISBN, TITLE, RELEASE_YEAR, PUBLISHER, THUMBNAIL, RATINGS, PRICE, AUTHOR
            in zip(datasets["ISBN"],
                   datasets["TITLE"],
                   datasets["RELEASE_YEAR"],
                   datasets["PUBLISHER"],
                   datasets["THUMBNAIL"],
                   datasets["RATINGS"],
                   datasets["PRICE"],
                   datasets["AUTHOR"],
                   )
        ]

        # Create Bulk_Books
        Book.objects.bulk_create(bulk_books, ignore_conflicts=False, batch_size=1000)
    print("Done!")