from django import forms
from .models import Product

class ProCreateForm (forms.ModelForm):
    name = forms.CharField(max_length=225)
    price = forms.IntegerField()
    image = forms.ImageField()
    cat_id = forms.IntegerField()

    class Meta:
        model = Product
        fields = ['name','price','image','cat_id']