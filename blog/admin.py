from django.contrib import admin
from .models import Author, Tag, Post, Comment

admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
