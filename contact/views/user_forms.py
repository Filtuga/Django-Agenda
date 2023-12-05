from django.shortcuts import render, redirect
from contact.forms import RegisterForm
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')

        if form.is_valid():
            form.save()
            messages.success(request, f"User <{username}> has been created.")
            return redirect('contact:login')
    context = {
        'form': form
    }

    return render(request, "contact/register.html", context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user=user)
            messages.success(request, "Logged In.")
            return redirect('contact:index')
        
    context = {
        'form': form
    }

    return render(request, "contact/login.html", context)



def logout_view(request):
    auth.logout(request)
    messages.info(request, "Logged out.")
    return redirect('contact:login')

