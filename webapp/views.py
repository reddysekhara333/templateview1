from django.shortcuts import render

# Create your views here.
def template(request):
    return render(request,'app/home.html')
def loginform(request):
    return render(request,'app/login.html')