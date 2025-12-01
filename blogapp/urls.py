
# Function Based Views Urls

# from django.urls import path
# from blogapp.views import post_list, post_detail, post_create, post_update, post_delete, posts_branch_by

# urlpatterns = [
#     path('', post_list, name='post_list'),
#     path('postdetail/<int:id>/', post_detail, name='post_detail'),
#     path('postcreate/', post_create, name='post_create'),
#     path('postupdate/<int:id>/', post_update, name='post_update'),
#     path('postdelete/<int:id>/', post_delete, name='post_delete'),
#     path('branch/<int:id>/', posts_branch_by, name='posts_branch_by'),
# ]




# Class Based Views Urls

from django.urls import path
from blogapp.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, BranchPostListView, OwnLoginView, OwnLogoutView, RegisterationView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('postdetail/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('postcreate/', PostCreateView.as_view(), name='post_create'),
    path('postupdate/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('postdelete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('branch/<int:pk>/', BranchPostListView.as_view() ,name='posts_branch_by'),
    
    # Auth. Urls
    path('login/', OwnLoginView.as_view(), name='login'),
    path('logout/', OwnLogoutView.as_view(), name='logout'),
    path('register/', RegisterationView.as_view(), name='register'),
]






