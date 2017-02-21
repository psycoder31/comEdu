from django import forms
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms import ModelForm
from .models import Comment, Post, Category
from django.contrib.auth.models import User

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)
        # widgets = {
        #     'message' : SummernoteWidget(),
        #     }
    # def save(self, commit=True, *args, **kwargs):
    #     obj = super(CommentForm, self).save(commit=False, *args, **kwargs)
    #     if commit:
    #         obj.save()
    #     return obj

class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', )
        widgets = {
            'content' : SummernoteWidget(),
            }
    # def save(self, commit=True, *args, **kwargs):
    #     obj = super(PostForm, self).save(commit=False, *args, **kwargs)
    #     if commit:
    #         obj.save()
    #     return obj
