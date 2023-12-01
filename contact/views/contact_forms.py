from django import forms
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from contact import models
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["first_name", "last_nome", "phone"]
        
    def clean(self):
        cleaned_data = self.cleaned_data
        
        self.add_error(
            "first_name",
            ValidationError("Mensagem de erro", code="invalid")
            );

# Create your views here.
def create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        context = {
            "form": form
        }
    
        return render(request, "contact/create.html", context)
    
    context = {
        "form": ContactForm(),
    }
    
    return render(request, "contact/create.html", context)


