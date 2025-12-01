from django.shortcuts import render, get_object_or_404, redirect
from blogapp.forms import PostForm, RegisterationFrom
from blogapp.models import Post, Branch
from django.contrib.auth import views
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView






# Create your views here.

# Function Based Views:

# def post_list(request):
#     posts = Post.objects.all().order_by('-created_at')
#     return render(request, 'blogapp/post_list.html', {'posts': posts})


# def post_detail(request, id):
#     post = get_object_or_404(Post, id=id)
#     return render(request, 'blogapp/post_detail.html', {'post': post})


# def post_create(request):
#     form = PostForm(request.POST or None)
    
#     if form.is_valid():
#         form.save()
#         return redirect('post_list')
    
#     return render(request, 'blogapp/post_create.html', {'form':form})


# def post_update(request, id):
#     post = get_object_or_404(Post, id=id)
#     form = PostForm(request.POST or None, instance=post)
    
#     if form.is_valid():
#         form.save()
#         return redirect('post_detail', id=post.id)
    
#     return render(request, 'blogapp/post_update.html', {'form': form})


# def post_delete(request, id):
#     post = get_object_or_404(Post, id=id)
    
#     if request.method == 'POST':
#         post.delete()
#         return redirect('post_list')
    
#     return render(request, 'blogapp/post_detail.html', {'post': post})


# def posts_branch_by(request, branch_id):
#     branch = get_object_or_404(Branch, id=branch_id)
#     posts = Post.objects.filter(branch=branch)
#     return render(request, 'blogapp/posts_branch_by.html', {'branch': branch, 'posts': posts})











# Class Based Views:

class RegisterationView(View):
    template_name = 'blogapp/register.html'
    
    def get(self, request, *args, **kwargs):
        form = RegisterationFrom()
        return render(request, self.template_name, {'from': form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterationFrom(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created successfully you can login now")
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    



class OwnLoginView(View):
    template_name = 'blogapp/login.html'
    
    def get(self ,request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data = request.POST)
    
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
        return render(request, self.template_name, {'form': form})
    

class OwnLogoutView(LogoutView):
    next_page = 'post_list'
    template_name = 'blogapp/logout.html'
    
    
    
class PostListView(ListView):
    model = Post
    template_name = 'blogapp/post_list.html'
    context_object_name = 'posts'
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogapp/post_detail.html'
    context_object_name = 'post'
    

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'branch', 'tags']
    template_name = 'blogapp/post_create.html'
    success_url = reverse_lazy('post_list')
    
    
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'branch', 'tags']
    template_name = 'blogapp/post_update.html'
    success_url = reverse_lazy('post_list')
    
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blogapp/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    

class BranchPostListView(ListView):
    model = Post
    template_name = 'blogapp/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        branch_id = self.kwargs("id")
        return Post.objects.filter(branch_id=branch_id)
        
    
    

    
    
    
    
    


    
    
    
    




