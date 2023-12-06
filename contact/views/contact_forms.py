from django.shortcuts import render, redirect, get_object_or_404
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from contact.forms import ContactForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required(login_url='contact:login')
def create_contact(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        context = {
            'form': form,
            'form_action': form_action
        }
        if form.is_valid():
            messages.success(request, "You Contact was added.")
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
        return redirect("contact:contact_detail", contact.id)

    context = {
        'form': ContactForm(),
        'form_action': form_action

    }
    return render(request, "contact/create_contact.html", context)


@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=[contact_id])

    if request.method == 'POST':
        print('POST method')
        form = ContactForm(request.POST, instance=contact)
        picture = request.FILES.get('picture')
        print(picture)
        if picture:
            contact.picture = picture
            contact.save()

        context = {
            'form': form,
            'form_action': form_action
        }
        if form.is_valid():
            contact = form.save()
            messages.success(request, "You Contact was updated.")
        return redirect("contact:update", contact.id)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action

    }
    return render(request, "contact/create_contact.html", context)


@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True)

    contact.delete()

    return redirect('contact:index')