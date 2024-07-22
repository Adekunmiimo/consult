from django.shortcuts import render, get_object_or_404
from .models import Card, HeroSection, InfoSection, Insight, Page, Partner

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)


    return render(request, 'page_detail.html', {'page': page})

def industries(request):
    return render(request, 'industries.html')
