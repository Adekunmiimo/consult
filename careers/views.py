from django.shortcuts import render, get_object_or_404
from .models import Card, HeroSection, InfoSection, Insight, Page, Partner

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)

    return render(request, 'home.html', {'page': page})

def careers(request):
    return render(request, 'careers.html')
