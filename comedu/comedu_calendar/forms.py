from django import forms
from django.db import models
from django.forms.extras.widgets import SelectDateWidget, SelectTimeWidget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils import timezone
from django.contrib.admin import widgets
from .models import CalendarEvent


class CalendarForm(forms.ModelForm):
    start = forms.DateField(widget = forms.TextInput(attrs={'class':'testDatepicker'}),initial = timezone.now(), required = True)
    # start_time = forms.TimeField(widget = SelectTimeWidget, initial = timezone.now())
    end = forms.DateTimeField(widget = SelectDateWidget, initial = timezone.now(), required = True)
    # end_time = forms.TimeField(widget = SelectTimeWidget, initial = timezone.now())
    title = forms.CharField(required = True)

    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify', 'author',)
        widgets = {
        'context': SummernoteWidget(),

        }
