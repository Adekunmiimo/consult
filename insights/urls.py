from django.urls import path
from .views import insights

urlpatterns = [
    # path('<slug:slug>/', page_detail, name='page_detail'),

    path('', insights, name='insights'),
]
