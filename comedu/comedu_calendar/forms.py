from django import forms
from django.db import models
from .models import CalendarEvent
from django.forms.extras.widgets import SelectDateWidget, SelectTimeWidget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils import timezone
from django.contrib.admin import widgets


class CalendarForm(forms.ModelForm):

    start = forms.DateTimeField(widget = SelectDateWidget,initial = timezone.now(), required = True)
    # start_time = forms.TimeField(widget = SelectTimeWidget, initial = timezone.now())
    end = forms.DateTimeField(widget = SelectDateWidget, initial = timezone.now())
    # end_time = forms.TimeField(widget = SelectTimeWidget, initial = timezone.now())
    title = forms.CharField(required = True)

    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify', 'author',)
        widgets = {
        'context': SummernoteWidget(),
        }
