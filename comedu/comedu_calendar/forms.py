from django import forms
from django.db import models
from .models import CalendarEvent
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone


class CalendarForm(forms.ModelForm):
    start = forms.DateTimeField(widget=SelectDateWidget, initial=timezone.now(), required = True)
    end = forms.DateTimeField(widget=SelectDateWidget, initial=timezone.now())
    title = forms.CharField(required = True)
    class Meta:
        model = CalendarEvent
        fields = ('title', 'context', 'start', 'end', 'classify',)


# class SearchForm(forms.Form):
#
#     CHOICE_FOR_SEARCH = (
#                         ('ti','title'),
#                         ('co','context'),
#                         )
#
#     category = forms.ChoiceField(required = False,
#                                 widget = forms.Select,
#                                 choices = CHOICE_FOR_SEARCH, )
#
#     search = forms.CharField(required = True)
        ##ordering = ('start',)왜 실행이 안될까?
