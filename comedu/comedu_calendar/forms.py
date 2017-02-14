from django import forms
from django.db import models
from .models import CalendarEvent

from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone


class CalendarForm(forms.ModelForm):
    start = forms.DateField(widget=SelectDateWidget, initial=timezone.now())
    end = forms.DateField(widget=SelectDateWidget, initial=timezone.now())

    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)
        ##ordering = ('start',)왜 실행이 안될까?


class CalendarForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)
