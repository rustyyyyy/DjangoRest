from django import forms
from .models import product

class productEdit(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"

class productAdd(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name', 'description', 'price','date']