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
        ('Tank', 'Танк'),
        ('Healer', 'Хил'),
        ('DD', 'ДД'),
        ('Trader', 'Торговец'),
        ('Guildmaster', 'Гильдмастер'),
        ('Questgiver', 'Квестгивер'),
        ('Blacksmith', 'Кузнец'),
        ('Leatherworker', 'Кожевник'),
        ('Alchemist', 'Алхимик'),
        ('Magicmaster', 'Мастер магии'),
    ]
    title = models.CharField(choices=cat_var, max_length=50)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


