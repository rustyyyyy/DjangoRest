from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import product,Brand
from .forms import productForm,BrandForm


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/product')
        else:
            messages.success(request,'error while loggin in')
            return redirect('login')
    else:
        return render(request,'authenticate\login.html',{})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    products = product.objects.all() 
    context = {'products':products}
    return render(request, 'base\home.html',context)


@login_required
def editProduct(request,pk):
    products = product.objects.get(id=pk)
    productform = productForm(instance=products)

    productObj=productForm(request.POST,instance=products)
    if request.method == 'POST':
        productObj.save()
        return redirect('home')
    context ={ 'form' : productform} 
    return render(request, 'base\product_form.html', context)


@login_required
def createProduct(request):
    productObj=productForm(request.POST)
    if request.method == 'POST':
        productObj.save()
        return redirect('home')
    context ={ 'form':productForm} 
    return render(request, 'base\product_form.html',context)


@login_required
def deleteProduct(request,pk):
    productObj = product.objects.get(id=pk)
    if request.method == 'POST':
        productObj.delete()
        return redirect('home')


@login_required
def brand(request):
    brands = Brand.objects.all()
    context = {'brands':brands}
    return render(request, 'base/brandList.html',context)


@login_required
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


@login_required
def deleteBrand(request,pk):
    brand = Brand.objects.get(id=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('brands')