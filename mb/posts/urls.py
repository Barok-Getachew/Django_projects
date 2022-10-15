from django.urls import path
from posts.views import *
urlpatterns = [
path('me/', HomePageView.as_view(), name='home'),
]