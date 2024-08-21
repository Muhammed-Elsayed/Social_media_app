from django.urls import path
from .views import LikeView , Unlike

urlpatterns = [
    path('like', LikeView.as_view(), name='like'),
    path('unlike/<int:pk>', Unlike.as_view(), name='unlike'),

 
]