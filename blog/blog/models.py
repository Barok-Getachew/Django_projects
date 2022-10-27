# Create your models here.
from unittest.util import _MAX_LENGTH
from django.db import models
class Post(models.Model) :
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.user',
        on_delete = models.CASCADE,
    )
    body = models.TextField()
    def __str__(self) :
        return self.title[:30]


