from django.urls import path
from .views import FollowView

urlpatterns = [
    #path('follow/', FollowView.as_view(), name='follow'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    path('unfollow/<int:user_id>/', FollowView.as_view(), name='unfollow'),
]
