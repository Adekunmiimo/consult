from django.urls import path
from .views import by_services

urlpatterns = [
    # path('<slug:slug>/', page_detail, name='page_detail'),

    # path('', insights, name='insights'),
    path('by_services/', by_services, name='by_service')
]
