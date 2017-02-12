from django import forms
from django.db import models
from .models import CalendarEvent
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

import django_filters

...
class CalendarForm(forms.ModelForm):
    start = forms.DateField(widget=SelectDateWidget, initial=timezone.now())
    end = forms.DateField(widget=SelectDateWidget, initial=timezone.now())
    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)


class CalendarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CalendarEvent
        fields = ['title', 'context','start', 'end', 'classify']

class Calendar_search(forms.Form):
    search_word = models.CharField(max_length = 20)
