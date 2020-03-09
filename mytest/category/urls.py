from django.urls import path
from .views import *

urlpatterns = [
    path ('cat/',all,name='cat-all'),
    path ('cat/create/',create,name='cat-create'),
    path ('cat/edit/<int:id>',edit,name='cat-edit'),
    path ('cat/delete/<int:id>',delete,name='cat-delete'),


]