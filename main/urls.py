from django import views
from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("delete/<int:empresa_id>/", views.delete, name="delete"),
    path("edit/<int:empresa_id>/", views.edit, name="edit"),
]