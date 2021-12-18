from django import forms
from .models import product,Brand

class productEdit(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"

class productAdd(forms.ModelForm):
    class Meta:
        model = product
        fields = ['name','brandname', 'description', 'price','date']

class BrandList(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"