from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def form(request):
    return  render(request,'form.html')

def navs(request):
    return render(request,'navs.html')

def image(request):
    return render(request,'image.html')

def description(request):
    return render(request,'description.html')

def ulist(request):
    return render(request,'ulist.html')
def olist(request):
    return render(request,'olist.html')