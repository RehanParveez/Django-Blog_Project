from django.shortcuts import render, get_object_or_404, redirect
from blogapp.forms import PostForm
from blogapp.models import Post, Branch

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blogapp/post_detail.html', {'post': post})


def post_create(request):
    form = PostForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('post_list')
    
    return render(request, 'blogapp/post_create.html', {'form':form})


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    
    if form.is_valid():
        form.save()
        return redirect('post_detail', id=post.id)
    
    return render(request, 'blogapp/post_update.html', {'form': form})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    
    return render(request, 'blogapp/post_detail.html', {'post': post})


def posts_branch_by(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    posts = Post.objects.filter(branch=branch)
    return render(request, 'blogapp/posts_branch_by.html', {'branch': branch, 'posts': posts})

    
    
    
    




