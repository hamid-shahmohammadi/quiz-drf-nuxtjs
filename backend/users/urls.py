from django.urls import path
from .views import RegisterView,LoginView,UserView,LogoutView,login,CurrentLoggedInUser

app_name='users'

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', login),
    # path('user', UserView.as_view()),
    path('user', CurrentLoggedInUser.as_view({'get': 'retrieve'}), name="current_user"),
    path('logout',LogoutView.as_view()),
    
]