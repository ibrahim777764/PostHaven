from django.db import models
from django.contrib.auth.models import User

# models.py

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    my_field = models.CharField(max_length=100, default='')  # add this line to define a new field with a default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



