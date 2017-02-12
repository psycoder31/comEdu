from django import forms
from django.db import models
from .models import CalendarEvent
import django_filters

...
class CalendarForm(forms.ModelForm):
    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)


class CalendarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = CalendarEvent
        fields = ['title', 'context','start', 'end', 'classify']
