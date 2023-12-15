from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

from contact.forms import RegisterForm, RegisterUpdateForm

def register(request):
    form = RegisterForm()
    
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário cadastrado com sucesso")
            return redirect("contact")

            
    context = {
        "form": form
    }
    return render(request, "contact/register.html", context)


def login_view(request):
    
    form = AuthenticationForm(request)
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            messages.success(request, "Logado com sucesso")
            auth.login(request, user)
            return redirect("login_user")
            
    context = {
        "form": form
    }
    return render(request, "contact/login.html", context)


def logout_view(request):
    auth.logout(request)
    return redirect("login_user")


def user_update(request):
    
    if request.method == "GET":
        form = RegisterUpdateForm(instance=request.user)

        context = {
            "form": form
        }
        return render(request, "contact/user_update.html", context)

    form = RegisterUpdateForm(data=request.POST, instance=request.user)
    context = {
            "form": form,
    }
    
    if form.is_valid():
        form.save()
        messages.success(request, "Dados atualizados com sucesso")
        return redirect("login_user")
    
    return render(request, "contact/user_update.html", context)