from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product,Brand
from .forms import productEdit,productAdd

def home(request):
    products = product.objects.all() 
    context = {'products':products}
    return render(request, 'base\home.html',context)

def editProduct(request,pk):
    products = product.objects.get(id=pk)
    brands = Brand.objects.all()
    productObj=productEdit(request.POST,instance=products)

    print(productObj)    
    if request.method == 'POST':
        productObj.save()
        return redirect('home')
    context ={ 'product' : products,'brands':brands} 
    return render(request, 'base\product_form.html', context)

def createProduct(request):
    productObj=productAdd(request.POST)
    brands = Brand.objects.all()
    if request.method == 'POST':
        productObj.save()
        return redirect('home')
    context ={ 'brands':brands} 
    return render(request, 'base\product_form.html',context)

def deleteProduct(request,pk):
    productObj = product.objects.get(id=pk)
    if request.method == 'POST':
        productObj.delete()
        return redirect('home')