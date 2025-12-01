from django import forms
from blogapp.models import Post, User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'branch', 'tags']
        
        
class RegisterationFrom(UserCreationForm):
    email = forms.EmailField()
    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
        

