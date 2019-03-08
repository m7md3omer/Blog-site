from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # this method is used to redirect the user to the created Post after creating or updating  it
    # django by default searches for this method after creating a post
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
