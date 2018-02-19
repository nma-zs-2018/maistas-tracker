from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.is_authenticated:
        print("Prisijunges")
    else:
        return redirect(signIn, permanent=True)

    return render(request, 'index.html')
    # return render(request, 'index.html', )

def signIn(request):
    with_info = (len(request.POST) > 0)

    if with_info:
        user = authenticate(username=request.POST['username'], password=request.POST['pass'])
        if user is not None:
            print("Prisijungta")
            login(request, user)
            return redirect(index, permanent=True)
        else:
            print("Neprisijungta")
    else:
        pass

    return render(request, 'login.html')

def signUp(request):

    return render(request, 'register.html')