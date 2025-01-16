from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from .models import *
from .forms import *


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def notification(request):
    notifications = Notification.objects.filter(recipient=request.user)
    return render(request, 'bboard/notifications.html', {'notifications': notifications})



#------------------------------------------------------------------
#отображение всех новостей и по одной новости отдельно


class PostListView(ListView):
    model = Post
    template_name = 'bboard/posts.html'
    context_object_name = 'posts'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'bboard/post_detail.html'
    context_object_name = 'post'

#-------------------------------------------------------------------
#создание и редактирование

class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'bboard/create_post.html'




class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'bboard/update_post.html'

    def get_success_url(self):
        return f'/update/{self.object.id}'


#------------------------------------------------------------------
#Комментарии к обьявлениям

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'bboard/add_comment.html'
    form_class = CommentForm

    def get_success_url(self):
        return f'/list_comments/{self.kwargs["pk"]}'


class CommentListView(ListView):
    model = Comment
    template_name = 'bboard/list_comments.html'
    context_object_name = 'comments'

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['pk'])


#------------------------------------------------------------------






