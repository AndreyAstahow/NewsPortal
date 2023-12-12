from django.contrib import admin
from .models import Author, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'post_class', 'author', 'rating')
    list_filter = ('headline', 'post_class', 'author', 'rating')
    search_fields = ('headline', 'post_class__name', 'author', 'rating')

# Register your models here.

admin.site.register(Author)
admin.site.register(Post, PostAdmin)