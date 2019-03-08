from django.urls import path
from .views import (PostListView,
                    PostCreateView,
                    PostDetailView,
                    PostUpdateView,
                    PostDeleteView,
                    about)

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    # pk is the default argument for primary keys so we don't have to tell the class about which instance to display
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/new/', PostCreateView.as_view(), name='create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('about/', about, name='about'),
]
