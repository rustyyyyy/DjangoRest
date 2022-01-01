from django import forms
from django import forms
from .models import product,Brand

class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = "__all__"
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control col-md-6'}),
            'brandname':forms.Select(attrs={'class':'form-control col-md-6'}),
            'date':forms.DateInput(attrs={'class':'form-control col-md-6','type':'date'}),
            'description':forms.TextInput(attrs={'class':'form-control col-md-6','type':'text'}),
            'price':forms.NumberInput(attrs={'class':'form-control col-md-6'})
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = "__all__"
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control col-md-6'}),
        }