from django.shortcuts import render


# Create your views here.
def index(request):
    
    context = {
        "texto": "Contact inicial"
    }
    
    return render(request, "contact/index.html", context)
