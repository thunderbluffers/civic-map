from django.contrib.auth.models import AbstractUser
from django.contrib.admin import ModelAdmin


class User(AbstractUser):
    pass

class UserAdmin(ModelAdmin):
    pass

