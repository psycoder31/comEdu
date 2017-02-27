from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
from django import forms

from django.contrib.auth.models import User

from .forms import CommentForm, PostForm, AlbumForm
from .models import Post, Comment, Category, AlbumPost


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
    return render_to_response(template_name, {'posts' : results, 'index' : category, 'slug':slug,})


def post_DV(request, pk):
    qs = Post.objects.get(pk=pk)
    cat = Category.objects.get(name = qs.category)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit = False)
                comment.post = Post.objects.get(pk=pk)
                comment.author = request.user
                comment.save()
                return redirect('/blog/post/%s' % (pk))
        else:
            return redirect ('/blog/not_admin')
    form = CommentForm()
    return render(request, 'blog/post_detail.html', {'form' : form, 'Post':qs, 'Cat' : cat})


def category_LV(request):

    qs = Category.objects.exclude( name = '공지사항')
    qs2 = Category.objects.get(name ='공지사항')

    return render(request, 'blog/category_all.html', {'categories' : qs, 'notice' : qs2})


def new_post(request, slug=None):
    if not request.user.is_authenticated:
        return render_to_response('blog/not_admin.html',)
    # elif slug == 'notice' and request.user.is_manager == False:
    #     return render_to_response('blog/not_admin.html',)
    else:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                newboard = form.save(commit=False)
                newboard.author = request.user
                cat = Category.objects.get(name=newboard.category)

                if cat.slug == '공지사항':

                    if request.user.is_manager == True :
                        newboard.save()
                        return redirect('/blog/%s' % (cat.slug))
                    else:
                        return render_to_response('blog/not_admin.html', )
                else :
                    newboard.save()
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
    if request.user == post.author or request.user.is_manager == True :
        return render(request, 'blog/post_edit.html', {'form' : form})
    else :
        return redirect ('/blog/not_admin')


def post_delete(request, pk=None):
    qs = Post.objects.get(pk=pk)
    sl = Category.objects.get(name = qs.category)
    if request.user == qs.author or request.user.is_manager == True :
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

            posts = Post.objects.filter(category=category, author__username__contains = q)

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


def album_LV(request):
    qs = AlbumPost.objects.all()
    template_name = 'blog/album_all.html'
    paginator = Paginator(qs, 6)
    page = request.GET.get('page', '1')
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return render_to_response( template_name, {'albums' : results})


def new_album(request):
    if not request.user.is_authenticated:
        return render_to_response('blog/not_admin.html',)
    else:
        form = AlbumForm()
        if request.method == "POST":
            form = AlbumForm(request.POST, request.FILES)
            # form.is_bound = True
            # form.data = request.POST
            # form.files = request.FILES
            if form.is_valid():
                newboard = form.save(commit=False)
                newboard.author = request.user
                newboard.save()
                return redirect('/blog/album')
            else :
                return redirect('/blog/album')
        return render(request, 'blog/new_album.html', {'form': form})
