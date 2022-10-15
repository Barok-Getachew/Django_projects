from django.shortcuts import render
from django.views.generic import ListView
from posts.models import post

class HomePageView(ListView) :
    model = post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
