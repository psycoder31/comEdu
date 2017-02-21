from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
# from django.template import RequestContext, loader
from django.http import HttpResponse
# from django.urls import reverse
from django.core.paginator import Paginator
from django.utils import timezone
from django import forms

from django.contrib.auth.models import User

from .forms import CommentForm, PostForm
from .models import Post, Comment, Category


def post_LV(request, slug):
    category = get_object_or_404(Category, slug=slug)
    model = Post.objects.filter(category=category)
    template_name='blog/post_all.html'

    paginator = Paginator(model, 6)
    page = request.GET.get('page', '1')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    return render(request, template_name, {'posts' : results, 'index' : category, 'slug':slug,})


def post_DV(request, pk):
    qs = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = Post.objects.get(pk=pk)
            comment.author = request.user
            comment.save()
            return redirect('/blog/post/%s' % (pk))
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form' : form, 'Post':qs})



def category_LV(request):
    qs = Category.objects.all()
    return render(request, 'blog/category_all.html', {'categories' : qs,})


def new_post(request, slug=None):
    if not request.user.is_authenticated:
        return render_to_response('blog/not_admin.html',)
    else:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                newboard = form.save(commit=False)
                newboard.author = request.user
                newboard.save()
                cat = Category.objects.get(name=newboard.category)
                return redirect('/blog/%s' % (cat.slug))
        else:
            form = PostForm()
        return render(request, 'blog/new_post.html', {'form': form})


def post_edit(request, pk=None):
    if pk :
        post = get_object_or_404(Post,id=pk)
    else :
        return HttpResponseForbidden()
    form = PostForm(request.POST or None, instance = post)
    if request.POST and form.is_valid():
        form.modify_date = forms.DateTimeField(timezone.now())
        form.author = request.user
        form.save()
        return redirect('/blog/post/%s' % (pk))
    if request.user == post.author :
        return render(request, 'blog/post_edit.html', {'form' : form})
    else :
        return redirect ('/blog/not_admin')


def post_delete(request, pk=None):
    qs = Post.objects.get(pk=pk)
    sl = Category.objects.get(name = qs.category)
    if request.user == qs.author :
        Post(pk=pk).delete()
        return redirect('/blog/%s' % (sl.slug))
    else :
        return redirect ('/blog/not_admin')

def post_search(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    if request.GET['category'] == 'ti':
        if request.GET['q']:
            q = request.GET['q']
            posts = Post.objects.filter(category=category, title__icontains = q)
            paginator = Paginator(posts, 6)
            page = request.GET.get('page', '1')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)
            return render_to_response('blog/post_all.html', {'posts':results, 'search':q, 'index': category, 'slug' : slug})
        else:
            return render_to_response('blog/post_all.html', {'error':True, 'index' : category, 'slug' : slug })
    if request.GET['category'] == 'co':
        if request.GET['q']:
            q = request.GET['q']
            posts = Post.objects.filter(category=category, content__icontains = q)
            paginator = Paginator(posts, 6)
            page = request.GET.get('page', '1')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)
            return render_to_response('blog/post_all.html', {'posts':results, 'search':q, 'index' : category, 'slug' : slug})
        else:
            return render_to_response('blog/post_all.html', {'error':True, 'index' :category, 'slug' : slug})
    if request.GET['category'] == 'au':
        if request.GET['q']:
            q = request.GET['q']
            posts = Post.objects.filter(category=category, author__username__contains = q) #작성자 검사 방법 찾기
            paginator = Paginator(posts, 6)
            page = request.GET.get('page', '1')
            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                results = paginator.page(1)
            except EmptyPage:
                results = paginator.page(paginator.num_pages)
            return render_to_response('blog/post_all.html', {'posts':results, 'search':q, 'index' : category, 'slug' : slug})
        else:
            return render_to_response('blog/post_all.html', {'error':True, 'index' :category, 'slug' : slug})

def not_admin(request):
    return render_to_response('blog/not_admin.html', )
