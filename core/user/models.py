from django.db import models
from core.abstract.models import AbstractManager, AbstractModel
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser


# Create your models here.
class UserManager(BaseUserManager, AbstractManager):
    def create_user(self, username, email, password=None, **kwargs):
        """
            Create and return a User with an email, username and password.
        """
        if not username:
            raise TypeError("Users must have a username.")
        elif not email:
            raise TypeError("Users must have an email.")
        elif not password:
            raise TypeError("Users must have a password.")

        # user.save(using=self._db) is saving the user object to the database using the database associated with the manager of the current model.
        # Normalize the email address by lowercasing the domain part of it
        # save into specific database using "using"
        # hashes the password before saving
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email, **kwargs):
        """
            Create and return a `User` with superuser (admin) permissions.
        """
        if not password:
            raise TypeError("Superusers must have a password.")
        elif not email:
            raise TypeError("Superusers must have an email.")
        elif not username:
            raise TypeError("Superusers must have an username.")

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    """
        db_index = True | for faster lookups
    """
    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # This will be prompted when creating a user
    REQUIRED_FIELDS = ['username']  # This will set to default login field

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"