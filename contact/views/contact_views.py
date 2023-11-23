from django.shortcuts import render, get_object_or_404, redirect
from contact import models
from django.db.models import Q
from django.http import Http404


# Create your views here.
def index(request):
    contacts = models.Contact.objects \
    .filter(show=True)\
    .order_by("-id")[:10]
    
    context = {
        "contacts": contacts,
        "site_title": "Contatos - "
    }
    
    return render(request, "contact/index.html", context)

def search(request):
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
        
        context = {
            "site_title": "Contatos - ",
            "contacts": contacts,
        }
        
        return render(request, "contact/index.html", context)

def contact(request, id):
 
    single_contact = get_object_or_404(
        models.Contact.objects, pk=id, show=True)
    
    context = {
        "contact": single_contact,
        "site_title": single_contact.__str__() + " - "
    }
    return render(request, "contact/contact.html", context)
