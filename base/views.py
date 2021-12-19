from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import product,Brand
from .forms import productForm,BrandForm

def home(request):
    products = product.objects.all() 
    context = {'products':products}
    return render(request, 'base\home.html',context)

def editProduct(request,pk):
    products = product.objects.get(id=pk)
    productform = productForm(instance=products)

    productObj=productForm(request.POST,instance=products)
    if request.method == 'POST':
        productObj.save()
        return redirect('home')
    context ={ 'form' : productform} 
    return render(request, 'base\product_form.html', context)

def createProduct(request):
    productObj=productForm(request.POST)
    if request.method == 'POST':
        productObj.save()
        return redirect('home')
    context ={ 'form':productForm} 
    return render(request, 'base\product_form.html',context)

def deleteProduct(request,pk):
    productObj = product.objects.get(id=pk)
    if request.method == 'POST':
        productObj.delete()
        return redirect('home')

def brand(request):
    brands = Brand.objects.all()
    context = {'brands':brands}
    return render(request, 'base/brandList.html',context)

def editBrand(request,pk):
    brands = Brand.objects.get(id=pk)
    brandform = BrandForm(instance=brands)
    editedbrand = BrandForm(request.POST,instance=brands)
    if request.method == 'POST':
        editedbrand.save()
        return redirect('brands')        

    context ={'form':brandform}
    return render(request, 'base/product_form.html',context)

def addBrand(request):
    newBrand  = BrandForm(request.POST)
    if request.method == 'POST':
        newBrand.save()
        return redirect('brands')
    context = {'form':BrandForm}
    return render(request, 'base\product_form.html',context)


def deleteBrand(request,pk):
    brand = Brand.objects.get(id=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brands')