from django.shortcuts import render

# Create your views here.


def mainView(request):
    template = 'index.html'
    return render(request, template, {})
