from django.db import models

from django.contrib.auth.models import User

class ques(models.Model):
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    tags=models.ForeignKey('tag',on_delete=models.CASCADE,null=True,blank=True)
    


class tag(models.Model):
    text=models.CharField(max_length=100)
    
class comments(models.Model):
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    comment_question=models.ForeignKey(ques,on_delete=models.CASCADE,null=True)
    comment_answer=models.ForeignKey('answers',on_delete=models.CASCADE,null=True)
    
class answers(models.Model):
    text=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)


