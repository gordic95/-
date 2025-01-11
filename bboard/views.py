from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django. contrib. auth. mixins import LoginRequiredMixin

from .models import *
from .forms import *

class PostListView(ListView):
    model = Post
    template_name = 'bboard/main.html'
    context_object_name = 'posts'
    ordering = ['-id']



class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'bboard/create_post.html'
    success_url = '/'


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'bboard/update_post.html'

    def get_success_url(self):
        return f'/update/{self.object.id}'


#_____________________________________________________________________






