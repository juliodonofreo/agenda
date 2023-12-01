from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from contact.forms import ContactForm

from contact import models
from contact.models import Contact

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


