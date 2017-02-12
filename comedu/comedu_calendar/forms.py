from django import forms
from django.db import models
from .models import CalendarEvent

class CalendarForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)
