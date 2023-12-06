from django.shortcuts import render, redirect
from contact.forms import RegisterForm, UserUpdateForm
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='contact:login')
def logout_view(request):
    auth.logout(request)
    messages.info(request, "Logged out.")
    return redirect('contact:login')

@login_required(login_url='contact:login')
def user_update(request):
    form = UserUpdateForm(instance=request.user)

    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been updated.")
            return redirect('contact:user_update')

    return render(request, 'contact/user_update.html', {'form': form})

