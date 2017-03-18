from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email")
        field_classes = {'username': UsernameField}
