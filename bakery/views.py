from django.shortcuts import render

# Create your views here.

def cake(request):
    return render(request,'bakery/cake.html')

def cakemenu(request):
    return render(request,'bakery/cakemenu.html')

def koreanmenu(request):
    return render(request,'bakery/koreanmenu.html')

def cookies(request):
    return render(request,'bakery/cookies.html')

def strawberries(request):
    return render(request,'bakery/strawberries.html')