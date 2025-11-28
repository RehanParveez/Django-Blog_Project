from django.contrib import admin
from blogapp.models import Branch, Tag, Post, OwnerProfile

# Register your models here.
@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['name']
  
  
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name'] 
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'branch']   
    

@admin.register(OwnerProfile)
class OwnerProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio']  
    
    
    


