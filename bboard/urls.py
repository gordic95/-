from django.urls import path
from .views import *



urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    path('create/', CreatePostView.as_view(), name='create_post'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update_post'),

    path('comment/<int:pk>', AddCommentView.as_view(), name='add_comment'),
    path('list_comments/<int:pk>', CommentListView.as_view(), name='list_comments'),

    path('notification/', notification, name='notification'),



    ]

