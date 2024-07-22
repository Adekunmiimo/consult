from django.urls import path
from .views import careers, page_detail

urlpatterns = [
    # path('<slug:slug>/', page_detail, name='careers_'),

    path('', careers, name='careers')
]
