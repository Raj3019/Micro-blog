from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30)
    post = models.TextField()

    def __str__(self):
        return self.title
