from django.urls import path
from .views import LikeView, CreateComment

urlpatterns = [
    path('like', LikeView.as_view(), name='like'),
    path('comment', CreateComment.as_view(), name='comment')
]