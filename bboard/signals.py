from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Comment, Notification


@receiver(post_save, sender=Comment)
def comment_posted(sender, instance, created, **kwargs):
    if created:
        post_author = instance.post.author
        comment_author = instance.author

        if post_author != comment_author:
            notification = Notification(recipient=post_author, actor=comment_author, verb=f'{comment_author.username} оставил комментарий к вашему объявлению', target=instance.post)
            notification.save()
