from django import forms
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms import ModelForm
from .models import Comment, Post, Category, AlbumPost
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', )
        widgets = {
            'content' : SummernoteWidget(),
            }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumPost
        fields = ('title', 'content', 'photo', )
