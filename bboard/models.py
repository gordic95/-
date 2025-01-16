from django.conf import settings
from django.db import models
from django.contrib.auth.models import User




class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, blank=True)


    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'/update/{self.id}'

    class Meta:
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'




class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey('Post', on_delete=models.PROTECT, null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'



class Category(models.Model):
    cat_var = [
        ("Танк", "Танк"),
        ("Хил", "Хил"),
        ("ДД", "ДД"),
        ("Торговец", "Торговец"),
        ("Гильдмастер", "Гильдмастер"),
        ("Квестгивер", "Квестгивер"),
        ("Кузнец", "Кузнец"),
        ("Кожевник", "Кожевник"),
        ("Алхимик", "Алхимик"),
        ("Мастер магии", "Мастер магии")
    ]

    title = models.CharField(choices=cat_var, max_length=50)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

#--------------------------------------------------
#Уведомления по комментариям к обьявлениям
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications', on_delete=models.CASCADE)
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    verb = models.CharField(max_length=255)
    target = models.ForeignKey(Post, blank=True, null=True, on_delete=models.SET_NULL)
    read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)



