from django import forms

from .models import PollModel

class PollForm(forms.ModelForm):

    class Meta:
        model  = PollModel
        fields = '__all__'
