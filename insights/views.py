from django.shortcuts import render, get_object_or_404
from .models import Card, HeroSection, InfoSection, Insight, Page, Partner

def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)

    career_page = Page.objects.all()
    hero = HeroSection.objects.all()
    info = InfoSection.objects.all()
    card = Card.objects.all()
    partner = Partner.objects.all()
    insight = Insight.objects.all()

    return render(request, 'page_detail.html', {'page': page, 'career_page': career_page, 'hero': hero, 'info':info, 'card': card, 'partner':partner, 'insight': insight})
