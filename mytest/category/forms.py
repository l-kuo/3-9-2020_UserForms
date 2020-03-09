from django import forms
from .models import Category
class CatCreateForm (forms.ModelForm):
    name = forms.CharField(max_length=225)

    class Meta :
        model = Category
        fields = ['name']