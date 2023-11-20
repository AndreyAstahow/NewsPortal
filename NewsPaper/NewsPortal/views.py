from django.views.generic import (
        ListView, DetailView, CreateView, DeleteView, UpdateView
    )
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Post
from .filters import  PostFilter
from .forms import PostForm

class PostList(ListView):
    model = Post
    ordering = 'time_create'
    template_name = 'flatpages/news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
       queryset = super().get_queryset()
       self.filterset = PostFilter(self.request.GET, queryset)
       return self.filterset.qs
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['filterset'] = self.filterset
       return context

class PostDetail(DetailView):
    model = Post
    ordering = 'author_id'
    template_name = 'flatpages/news_split.html'
    context_object_name = 'news'

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.add_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_class = 'news'
        return super().form_valid(form)

class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/news_edit.html'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('news_list')

class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('NewsPortal.add_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/articles_edit.html'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.post_class = 'article'
        return super().form_valid(form)
    
class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('NewsPortal.change_post')
    form_class = PostForm
    model = Post
    template_name = 'flatpages/articles_edit.html'

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('news_list')
