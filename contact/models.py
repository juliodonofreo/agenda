from django.contrib.auth import get_user_model
from django.db import models


class Category(models.Model):  
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "categories"
        
    name = models.CharField(max_length=50, default="SEM NOME")


    def __str__(self) -> str:
        return f"{self.name}"
        


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50, help_text="Texto de ajuda para seu usuário")
    last_nome = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/")

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_nome}"
