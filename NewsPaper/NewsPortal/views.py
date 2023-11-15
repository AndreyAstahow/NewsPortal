from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = 'time_create'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    ordering = 'author_id'
    template_name = 'flatpages/news_split.html'
    context_object_name = 'news'