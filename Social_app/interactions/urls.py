from django.urls import path
from .views import LikeView, UnlikeView

urlpatterns = [
    path('like', LikeView.as_view(), name='like'),
    path('unlike', UnlikeView.as_view(), name='unlike'),
]