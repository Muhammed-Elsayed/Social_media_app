from django.urls import path, include
from .views import RegisterView, LoginView, LogoutView, AllUsers

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout',LogoutView.as_view()),
    path('Allusers', AllUsers.as_view())
]
