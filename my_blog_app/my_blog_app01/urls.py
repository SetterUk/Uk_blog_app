
from django.urls import path,include
# from . import views
from .views import HomeView,articleDetailView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    # path("",views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path('article/<int:pk>/', articleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/<int:pk>/update/', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    
    ]
