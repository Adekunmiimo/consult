from django.shortcuts import render, get_object_or_404
from .models import Page

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'page_detail.html', {'page': page})

def abt(request):
    return render(request, 'abt.html')


def maxi(request):
    return render(request, 'maxi.html')

def drive(request):
    return render(request, 'drive.html')
