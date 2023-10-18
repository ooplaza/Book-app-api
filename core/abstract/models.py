"""
    When Defining a Custom Manager, "models.Manager" should be inherited.
"""
import uuid
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


class AbstractModel(models.Model):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        """
        When abstract is set to True, it means that the model is intended to be used as an abstract base class.
        Abstract base classes are not meant to be instantiated or used to create database tables on their own.
        Instead, they provide a common set of fields and methods that can be inherited by other concrete models.
        In other words, they serve as a blueprint for other models but do not represent a table in the database.
        """
        abstract = True
