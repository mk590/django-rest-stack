from django.db import models

from django.contrib.auth.models import User

class ques(models.Model):
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    # Views
    # Upvotes
    created_at=models.DateTimeField(auto_now_add=True)
    # tags=
    # comments=models.IntegerField()
    # answers


class tags(models.Model):
    text=models.CharField(max_length=100)
    
class comments(models.Model):
    # (text, author name, created_time
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    
class answers(models.Model):
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    comments=models

