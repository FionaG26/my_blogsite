from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Move the index path to the top
    path('post/', PostListView.as_view(), name='post_list'),  # Add 'post/' to the path
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
