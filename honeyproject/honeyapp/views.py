from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')

def land_page(request):
        return render(request,'gg.html')