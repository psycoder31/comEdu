from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from django.template import RequestContext
from .forms import CommentForm, NewForm
from .models import Post, Comment
from django.utils import timezone
from django import forms

class PostLV(ListView):
    model = Post
    template_name='blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 6

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('/blog/post/%s' % (pk))
        else:
            form = CommentForm()
            return render(request, 'blog/post_form.html', {'form' : form,})
    return render(request, 'blog/post_form.html', {'form' : CommentForm(),})

def new_post(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        if request.method == "POST":
            form = NewForm(request.POST)
            if form.is_valid():
                newboard = form.save(commit=False)
                newboard.save()
                return redirect('/blog/')
        else:
            form = NewForm()
        return render(request, 'blog/new_post.html', {'form': form})

def post_edit(request, pk=None):
    if pk :
        post = get_object_or_404(Post,id=pk)
    else :
        return HttpResponseForbidden()
    form = NewForm(request.POST or None, instance = post)
    if request.POST and form.is_valid():
        form.modify_date = forms.DateTimeField(auto_now_add = True)
        form.save()
        return redirect('/blog/post/%s' % (pk))
    return render(request, 'blog/post_edit.html', {'form' : form})

def post_delete(request, pk=None):
    Post(pk=pk).delete()
    return redirect('/blog/')
