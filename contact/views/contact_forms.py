from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST


from contact import models


# Create your views here.
def create(request):

    print(request.method)

    if(request.method == "POST"):
        post = request.POST
        
        for chave, valor in post.items():
            print(chave, valor)

    context = {
        
    }
    
    return render(request, "contact/create.html", context)

