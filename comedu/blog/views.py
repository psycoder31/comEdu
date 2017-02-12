from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView
from .forms import CommentForm
from blog.models import Post

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
            comment.post = Post.object.get(pk=pk)
            comment.save()
            return redirect('blog.views.PostDV', pk)
        else:
            form = CommentForm()
        return render(request, 'post_form.html', {'form' : form,})
