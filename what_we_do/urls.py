from django.urls import path
from .views import abt, page_detail

urlpatterns = [
    path('about/', abt, name='abt'),
    
]
