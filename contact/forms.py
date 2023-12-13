from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "accept": "image/*"
            }
        )
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["first_name"].widget.attrs.update({
            "class": "classe-a classe-bacon",
            "placeholder": "Escreva aqui"
        })


    class Meta:
        model = Contact
        fields = ["first_name", "last_nome", "phone",
                  "email", "description", "category",
                  "picture"]
        

    def clean(self):
        cleaned_data = self.cleaned_data

        first_name = cleaned_data.get("first_name", "")
        last_nome = cleaned_data.get("last_nome", "")

        if first_name == last_nome:
            self.add_error(
                "first_name",
                ValidationError("Primeiro nome não pode ser igual ao segundo", code="invalid")
            )

            self.add_error(
                "last_nome",
                ValidationError("Primeiro nome não pode ser igual ao segundo", code="invalid")
            )
        super().clean()


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "first_name", "last_name"]