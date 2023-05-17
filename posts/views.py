from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post


def get_index(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/index.html", context=context)


def get_post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "posts/post_detail.html", {"post": post})


def get_contacts(request):
    context = {"title": "Контакты"}
    return render(request, "posts/contacts.html", context=context)


def get_about(request):
    context = {"title": "О нас"}
    return render(request, "posts/about.html", context=context)