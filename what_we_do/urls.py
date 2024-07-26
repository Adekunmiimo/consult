from django.urls import path
from .views import abt, page_detail, maxi, drive, cloud1

urlpatterns = [
    path('about/', abt, name='abt'),
    path('maxi/', maxi, name='maxi'),
    path('drive/', drive, name='drive'),
    path('cloud1/', cloud1, name='cloud1'),
]
