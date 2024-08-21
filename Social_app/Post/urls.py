from django.urls import path
from .views import CreatePost, DeletePost , PostListView

urlpatterns = [
    path('createpost', CreatePost.as_view(), name='follow'),
    path('deletepost/<int:pk>', DeletePost.as_view(), name='post-delete'),
    path('getallposts', PostListView().as_view())
]
