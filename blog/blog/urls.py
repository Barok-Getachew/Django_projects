from django.urls import path
from .views import blogListView,BlogDetailView
urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('',blogListView.as_view(), name='home')
]
