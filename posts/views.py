from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from users.models import Profile

# Create your views here.

def posts_list(request):
    """"""

    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', { 'posts': posts })


@login_required(login_url='/accounts/login')
def posts_user(request):
    """"""
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/posts_list.html', { 'posts': posts })


@login_required(login_url='/accounts/login')
def post_new(request):
    """"""

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', { 'form': form })


@login_required(login_url='/accounts/login')
def post_edit(request, id):
    """"""
    current_post = Post.objects.get(id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=current_post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:list')
    else:
        form = PostForm(instance=current_post)

    return render(request, 'posts/post_form.html', { 'form': form })


def post_page(request, id):
    """"""

    post = Post.objects.get(id=id)
    return render(request, 'posts/post_page.html', { 'post': post })


@login_required(login_url='/accounts/login')
def post_delete(request, id):
    """"""

    post = Post.objects.get(id=id, author=request.user.id)

    if post is not None:
        post.delete()
        
    return redirect('posts:my_list')
