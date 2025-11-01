from django.urls import path
from .views import( 
   PostListView, 
   PostDetailView,
   PostCreateView,
   PostUpdateView,
   PostDeleteView,
   UserPostListView,
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('post/new/', PostCreateView.as_view(), name='post-Create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-Update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-Delete'),

]
