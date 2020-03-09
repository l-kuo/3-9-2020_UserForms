from django.urls import path
from .views import *

urlpatterns = [

    path ('',all,name='pro-all'),
    path ('create/',create,name='pro-create'),
    path ('edit/<int:id>',edit,name='pro-edit'),
    path ('delete/<int:id>',delete,name='pro-delete'),

]