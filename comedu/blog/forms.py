from django import forms
from .models import Comment, Post
from django.utils import timezone

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message')

class NewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo')
