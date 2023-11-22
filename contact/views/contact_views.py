from django.shortcuts import render, get_object_or_404
from contact import models
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


def contact(request, id):
 
    single_contact = get_object_or_404(
        models.Contact.objects, pk=id, show=True)
    
    context = {
        "contact": single_contact,
        "site_title": single_contact.__str__() + " - "
    }
    return render(request, "contact/contact.html", context)
