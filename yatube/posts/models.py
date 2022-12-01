from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
NUMBER_OF_LETTERS = 15


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
    )
    group = models.ForeignKey(
        'Group',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='posts',
    )

    def __str__(self):
        # выводим текст поста
        return self.text[:NUMBER_OF_LETTERS]


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=30, unique=True)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title[:NUMBER_OF_LETTERS]
