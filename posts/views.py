from django.views.generic import ListView, CreateView, UpdateView, DeleteView # new
from django.urls import reverse_lazy  # new



# from django.contrib.auth.decorators import login_required
#
from .forms import PostForm  # new
from .models import Post

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

# def edit_post(request, id):
#     post = get_object_or_404(Post, id=id)

#     if request.method == 'GET':
#         context = {'form': PostForm(instance=post), 'id': id}
#         return render(request,'post.html',context)

# def get_latest_posts(self):
#         return self.posts_set.all().order_by("-created_on")

class HomePageView(ListView):
    queryset = Post.objects.all().order_by("-created_at")
    model = Post
    template_name = "home.html"

# @login_required
class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url = "/"

# @login_required
class UpdatePostView(UpdateView):  # new
    model = Post
    form_class = PostForm
    template_name = "post.html"
    success_url ="/"
    # success_url = reverse_lazy("")

class DetailPostView(DeleteView):  # new
    model = Post
    template_name = "detail.html"
    # success_url = reverse_lazy("")

class DeltePostView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url ="/"
  