from django.shortcuts import render

# Create your views here.

def signaction(request):
    return render(request,"signup.html")