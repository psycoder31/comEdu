from django.shortcuts import render, redirect, render_to_response
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from django.template import RequestContext
from .forms import CommentForm
from .models import Post

class PostLV(ListView):
    model = Post
    template_name='blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 5

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
            return render_to_response('blog/post_detail.html', RequestContext(request,{'object':comment.post}))
        else:
            form = CommentForm()
            return render(request, 'blog/post_form.html', {'form' : form,})
    return render(request, 'blog/post_form.html', {'form' : CommentForm(),})
