from .models import Contact
from django.forms import ModelForm


class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "email",
        "description", "picture", "category", "owner",)

