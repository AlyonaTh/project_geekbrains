from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentsForm


class PostView(View):
    """Output of Posts"""

    def get(self, request):
        posts = Post.objects.all().order_by('-id')
        return render(request, 'blog.html', {'post_list': posts})


class PostDetail(View):
    """A special site for a Post"""

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'blog_detail.html', {'post': post})


class AddComments(View):
    """Left Comments"""

    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form = form.save()
        return redirect(f'/blog/{pk}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class AddLike(View):
    """To add Likes"""
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id=pk)
            return redirect(f'/blog/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id = int(pk)
            new_like.save()
            return redirect(f'/blog/{pk}')


class DelLike(View):
    """To delete Likes"""
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            like = Likes.objects.get(ip=ip_client)
            like.delete()
            return redirect(f'/blog/{pk}')
        except:
            return redirect(f'/blog/{pk}')
