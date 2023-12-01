from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm



def create_contact(request):
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
        return render(request, "contact/create_contact.html", context)

    context = {
        'form': ContactForm()
    }
    return render(request, "contact/create_contact.html", context)