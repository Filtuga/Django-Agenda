from .models import Contact
from django.forms import forms


class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields = '__all__'