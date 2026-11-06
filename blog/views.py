from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User

def home(request):
    return render(request, "blog/home.html")

def post_list(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        image = request.FILES.get("image")

        user = User.objects.first()

        Post.objects.create(
            title=title,
            content=content,
            image=image,
            author=user
        )

        return redirect("post_list")

    return render(request, "blog/post_create.html")