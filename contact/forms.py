from django import forms
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from contact.models import Contact


class ContactForm(forms.ModelForm):
    
    picture = forms.ImageField(
        allow_empty_file=True,
        required=False,
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
    first_name = forms.CharField(
        required=True, 
        min_length=3,
        )
    
    last_name = forms.CharField(
        required=True, 
        min_length=3,
        )
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = get_user_model()
        fields = [
            "first_name","last_name", "email","username"]
        
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email", None)
        
        user = get_user_model()
        
        if user.objects.filter(email=email):  # Estruturas de dados vazias retornam False, isto que está sendo checado aqui
            raise ValidationError(message={
                "email": "Este email já existe",
                },
                code="invalid")
            
        return cleaned_data

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True, 
        min_length=3,
        )
    
    last_name = forms.CharField(
        required=True, 
        min_length=3,
        )
    
    email = forms.EmailField(required=True)
    
    password = forms.CharField(
        label="Senha",
        required=False, 
        min_length=8,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html())
    
    password2 = forms.CharField(
        label="Confirmar senha",
        required=False, 
        min_length=8,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text="Use a mesma senha que antes")
    
    
    class Meta:
        model = get_user_model()
        fields = [
            "first_name","last_name", "email", "password", "password2"]
        
        
    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email", None)
        current_email = self.instance.email
        
        user = get_user_model()
        
        if user.objects.filter(email=email) and current_email != email:  # Estruturas de dados vazias retornam False, isto que está sendo checado aqui
             self.add_error("email", ValidationError("Este email já existe"))
        return email
          
            
    def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        
        if password:
            try:
                password_validation.validate_password(password)
            except ValidationError as errors:
                self.add_error("password", ValidationError(errors))
                return password
                
        return password
    
    
    def clean_password2(self):
        cleaned_data = super().clean()
        password2 = cleaned_data.get("password2")
        
        return password2
        
        
    def clean(self):    
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
                
        if password1 is None or password2 is None:
            return super().clean()

        if password1 != password2:
            self.add_error("password2",
                            ValidationError("Senhas não batem"))

        return super().clean()
    

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = get_user_model().objects.get(username=self.instance.username)
        
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")

        if password:
            user.set_password(password)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        if commit:
            user.save()

        return user