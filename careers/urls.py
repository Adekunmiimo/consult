from django.urls import path
from .views import careers

urlpatterns = [
    # path('<slug:slug>/', page_detail, name='careers_'),

    path('', careers, name='careers')
]
