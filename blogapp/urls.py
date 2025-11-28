from django.urls import path
from blogapp.views import post_list, post_detail, post_create, post_update, post_delete, posts_branch_by

urlpatterns = [
    path('', post_list, name='post_list'),
    path('postdetail/<int:id>/', post_detail, name='post_detail'),
    path('postcreate/', post_create, name='post_create'),
    path('postupdate/<int:id>/', post_update, name='post_update'),
    path('postdelete/<int:id>/', post_delete, name='post_delete'),
    path('branch/<int:id>/', posts_branch_by, name='posts_branch_by'),
]
