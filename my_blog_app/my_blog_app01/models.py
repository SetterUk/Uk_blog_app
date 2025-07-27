from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
class category(models.Model):
    name = models.CharField(max_length=100, default='General')
    def __str__(self):
        return self.title + " by " + str(self.author.username)
    

    def get_absolute_url(self):
        return reverse('article_detail',args = (str(self.id),))
       

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField( max_length=255)
    title_tag = models.CharField( max_length=255, default='My Blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=100, default='General')

    def __str__(self):
        return self.title + " by " + str(self.author.username)
    

    def get_absolute_url(self):
        return reverse('article_detail',args = (str(self.id),))
       