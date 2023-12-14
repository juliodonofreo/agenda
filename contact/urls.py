"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from contact import views

urlpatterns = [
    path("", views.index, name="contact"),
    path("search/", views.search, name="search"),
    
    # contact (CRUD)
    path("contact/<int:id>/detail/", views.contact, name="single_contact"),
    path("contact/create/", views.create, name="create_contact"),
    path("contact/<int:id>/update/", views.update, name="update_contact"),
    path("contact/<int:id>/delete/", views.delete, name="delete_contact"),
    
    # user
    path("user/create/", views.register, name="create_user"),
    path("user/login/", views.login_view, name="login_user"),
    path("user/logout/", views.logout_view, name="logout_user")


    
]
