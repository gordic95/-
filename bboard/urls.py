from django.urls import path
from .views import *



urlpatterns = [
    path('', PostListView.as_view(), name='main'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),



    ]

