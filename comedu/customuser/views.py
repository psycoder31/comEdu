from django.shortcuts import render

# Create your views here.


def mainView(request):
    template = 'customuser/index.html'
    return render(request, template, {})
