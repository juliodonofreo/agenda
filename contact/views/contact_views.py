from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest, HttpResponse

from contact import models


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    contacts = models.Contact.objects \
    .filter(show=True)\
    .order_by("-id")
    
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        "page_obj": page_obj,
        "site_title": "Contatos - "
    }
    
    return render(request, "contact/index.html", context)

def search(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        value = request.GET.get("q", "").capitalize().strip()
        
        if value == "":
            return redirect("contact")
        contacts = models.Contact.objects\
            .filter(show=True)\
                .filter(
                    Q(first_name__icontains=value) |
                    Q(last_nome__icontains=value) |
                    Q(email__icontains=value))
                
        paginator = Paginator(contacts, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        
        context = {
            "site_title": "Contatos - ",
            "page_obj": page_obj,
        }
        
        return render(request, "contact/index.html", context)

def contact(request: HttpRequest, id: int) -> HttpResponse:
 
    single_contact = get_object_or_404(
        models.Contact.objects, pk=id, show=True)
    
    context = {
        "contact": single_contact,
        "site_title": single_contact.__str__() + " - "
    }
    return render(request, "contact/contact.html", context)
