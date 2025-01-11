from django.urls import path
from .views import *



urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('create/', CreatePostView.as_view(), name='create'),
    ]

