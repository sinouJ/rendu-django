from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils import timezone

from .forms import PostForm
from .models import Post

def projets_view(request):
    posts = Post.objects.filter(is_published = 'True').order_by('published_date')
    drafts = Post.objects.filter(is_published = 'False').order_by('created_date')
    users = User.objects.all()

    return render(
        request, 
        'nos_projets/index.html', 
        {
            'posts': posts,
            'drafts': drafts,
            'users': users
        }
    )

def post_view(request, id):
    post = get_object_or_404(Post, id = id)
    page_title = post.title + ' | Post'
    return render(request, 'nos_projets/post_view.html', {'post': post, 'page_title': page_title})

def post_new(request):
    page_title = 'Créer un post'

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.is_published = False
            post.img = request.FILES['img']
            post.save()
            return redirect('post_view', id = post.id)
        
        else:
            return render(request, 'nos_projets/post_new.html', {'form': form, 'page_title': page_title})

    else:
        form = PostForm()
        return render(request, 'nos_projets/post_new.html', {'form': form, 'page_title': page_title})

def post_edit(request, id):
    page_title = 'Éditer un post'

    post = get_object_or_404(Post, id = id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)

        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.is_published = False
            post.save()
            return redirect('post_view', id=post.id)

    else:
        form = PostForm(instance = post)
        return render(request, 'nos_projets/post_new.html', {'form': form, 'page_title': page_title})

def publish_post(request, id):
    post = get_object_or_404(Post, id = id)

    post.publish()

    return redirect('projets_view')

def archive_post(request, id):
    post = get_object_or_404(Post, id = id)

    post.draft()

    return redirect('projets_view')