from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.


def mainView(request):
    template = 'index.html'
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            pass
    return render(request, template, {})


#temp
