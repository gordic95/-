from django import forms
from django.http import Http404

from .models import *


# Форма создания поста

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'cat']

#------------------------------------------------------------------
# Форма создания комментария
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def form_valid(self, form):
        comment = form.save(commit=False)
        try:
            comment.post = Post.objects.get(pk=self.kwargs['pk'])
            comment.author = self.request.user
            comment.save()
            return super().form_valid(form)
        except Post.DoesNotExist:
            return Http404('Пост не найден')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])
        return context
