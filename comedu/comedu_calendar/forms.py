from django import forms
from django.db import models
from .models import CalendarEvent
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone


class CalendarForm(forms.ModelForm):
    start = forms.DateTimeField( widget = SplitDateTimeWidget, initial = timezone.now(), required = True)
    end = forms.DateTimeField(widget = SplitDateTimeWidget, initial = timezone.now())
    title = forms.CharField(required = True)
    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)
