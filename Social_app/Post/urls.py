from django.urls import path
from .views import CreatePost, PostListView

urlpatterns = [
    path('post', CreatePost.as_view(), name='follow'),
    path('getallposts', PostListView().as_view())
]
