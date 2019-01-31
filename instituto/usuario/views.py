from django.shortcuts import render,redirect
# Create your views here.

def Principal(request):
    
    return render(request, 'usuarios.html')