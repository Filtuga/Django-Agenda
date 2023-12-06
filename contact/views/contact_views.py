from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    contacts = Contact.objects.filter(show=True)

    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, "contact/index.html", context)


def contact_detail(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id, show=True)
    except:
        raise Http404()


    context = {
        'contact': contact
    }

    return render(request, "contact/contact_detail.html", context)


def search(request):
    search_result = request.GET.get('q', '').strip()

    if search_result == '':
        redirect('contact:index')

    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_result) | Q(phone__icontains=search_result) | Q(email__icontains=search_result)
        )
    
    paginator = Paginator(contacts, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }

    return render(request, "contact/index.html", context)
