from django.contrib import admin
from core.user.models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "public_id",
        "username",
        "email",
        "first_name",
        "last_name",
        "bio",
        "avatar",
        "created",
        "is_active",
        "is_superuser",
    ]