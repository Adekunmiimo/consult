from django.urls import path
from .views import industries, page_detail

urlpatterns = [
    # path('<slug:slug>/', page_detail, name='page_detail'),
    path('industries/', industries, name='industries'),
]
