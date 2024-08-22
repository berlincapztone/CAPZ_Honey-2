from django.shortcuts import render

def landing_page(request):
    return render(request, 'index.html')

def land_page(request):
        return render(request,'gg.html')