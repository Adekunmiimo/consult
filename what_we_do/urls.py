from django.urls import path
from .views import abt, page_detail

urlpatterns = [
    # path('<slug:slug>/', page_detail, name='page_detail'),

    path('about/', abt, name='abt'),
]
