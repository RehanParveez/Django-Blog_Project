from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    title = models.CharField(max_length=60)
    content = models.TextField()
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class OwnerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username
    
    