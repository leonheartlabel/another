from django.urls import path

from .views import HomePageView, CreatePostView, UpdatePostView, DeltePostView,DetailPostView# new   
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", HomePageView.as_view(), name="posts"),
    # path('post/create', views.create_post, name='post-create'),
    # path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('update/<pk>', login_required(UpdatePostView.as_view()), name="edit_post"),
    path('post/<pk>', DetailPostView.as_view(), name="view_post"),
    path('delete/<pk>', login_required(DeltePostView.as_view()), name="delete_post"),
    path("post/", login_required(CreatePostView.as_view()), name="add_post")  # new
]