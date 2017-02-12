from django.shortcuts import render

from .forms import PollForm
# Create your views here.

def poll_new(request):
    form = PollForm()
    return render(request, 'polls/poll_new.html', {'form' : form})
