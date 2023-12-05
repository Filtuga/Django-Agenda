from .models import Contact
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email",
        "description", "picture", "category", "owner",)


class RegisterForm(UserCreationForm):

    fields = "__all__"

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('This e-mail is already registered', code='invalid'))

        return email
