from django.shortcuts import render, get_object_or_404

# def page_detail(request, slug):
#     page = get_object_or_404(Page, slug=slug)
#     return render(request, 'page_detail.html', {'page': page, })

# def insights(request):
#     return render(request, 'industries.html')


def by_services(request):
    return render(request, 'by_services.html')