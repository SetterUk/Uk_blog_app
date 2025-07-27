
from django.urls import path
from .views import userRegisterView

urlpatterns = [
    path('register/', userRegisterView.as_view(), name='register'),
    # The login path below is incorrect and conflicts with django.contrib.auth.urls
    # path('login/', userRegisterView.as_view(), name='login'),
    
    # path('logout/', userLogoutView.as_view(), name='logout'),
   
    
]
