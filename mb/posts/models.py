from cgitb import text
from django.db import models

class post(models.Model) :
    text = models.TextField()

    def __str__(self) :
     return self.text[:50]
