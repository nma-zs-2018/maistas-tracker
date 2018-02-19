from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from maistas.models import Food


def home(request):
    food_types = Food.objects.all()

    return render(request, 'index.html', context={'food_types': food_types})

# def index(request):
#     if request.user.is_authenticated:
#         return render(request, 'index.html')
#     else:
#         return redirect(signIn, permanent=True)
#
#     return render(request, 'index.html')
#
# def signIn(request):
#     with_info = (len(request.POST) > 0)
#
#     if with_info:
#         user = authenticate(username=request.POST['username'], password=request.POST['pass'])
#         if user is not None:
#             login(request, user)
#             return redirect(index, permanent=True)
#
#     return render(request, 'login.html')
#
# def signUp(request):
#     return render(request, 'register.html')
#
# def signOut(request):
#     print("logoutas")
#     logout(request)
#
#     return HttpResponse("")
#     #return redirect(signIn, permanent=True)