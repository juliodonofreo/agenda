from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


# Create your views here.
def create(request: HttpRequest) -> HttpResponse:
    
    form_action = reverse("create_contact")
    
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        context = {
            "form": form,
            "form_action": form_action
        }

        if form.is_valid():
            contact = form.save()
            return redirect("update_contact", id=contact.id)
        return render(request, "contact/create.html", context)

    context = {
        "form": ContactForm(),
        "form_action": form_action
    }

    return render(request, "contact/create.html", context)


def update(request, id):
    contact = get_object_or_404(
        Contact, id=id, show=True
    )
    form_action = reverse("update_contact", args=(id,))
    
    if request.method == "POST":
        form = ContactForm(data=request.POST, instance=contact)
        context = {
            "form": form,
            "form_action": form_action
        }

        if form.is_valid():
            contact = form.save()
            return redirect("update_contact", id=contact.id)
        return render(request, "contact/create.html", context)

    context = {
        "form": ContactForm(instance=contact),
        "form_action": form_action
    }

    return render(request, "contact/create.html", context)


def delete(request, id):
    contact = get_object_or_404(
        Contact, id=id, show=True
    )
    contact.delete()
    
    return redirect("contact")