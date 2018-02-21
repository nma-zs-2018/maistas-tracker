from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from maistas.models import Food, Order
from django.http import JsonResponse


def home(request):
    if not request.user.is_authenticated:
        return redirect('account_login', permanent=True)

    user_order = Order.objects.filter(deliver_to=request.user, main=True)
    has_order = (len(user_order) != 0)
    order_waiting = None

    if has_order:
        order_waiting = user_order[0].deliver_by is None

    print(has_order, order_waiting)

    food_types = Food.objects.all()

    query = User.objects.filter(username=request.user.username, groups__name__in=['Deliverers'])
    is_deliverer = len(query)

    return render(request, 'index.html', context={
        'has_order': has_order,
        'food_types': food_types,
        'is_deliverer': is_deliverer,
        'order_waiting': order_waiting
    })


def order(request):
    if request.user.is_authenticated:
        # Check if user already has any orders
        if len(Order.objects.filter(deliver_to=request.user)) == 0:
            print(request.POST)
            main_created = False
            for foodType in Food.objects.all():
                q = request.POST[str(foodType.id)]

                if int(q) > 0:
                    new_order = Order(
                        deliver_to=request.user,
                        deliver_by=None,
                        deliver_to_lat=None,
                        deliver_to_long=None,
                        current_delivery_lat=None,
                        current_delivery_long=None,
                        food=foodType,
                        quantity=q,
                        main=(not main_created),
                    )

                    if not main_created:
                        main_created = True
                        print(request.POST['lat'], request.POST['long'])
                        new_order.deliver_to_lat = request.POST['lat']
                        new_order.deliver_to_long = request.POST['long']

                    new_order.save()

            if not main_created:
                return JsonResponse({'success': False, 'error_message': 'No foods were selected.'})

            return JsonResponse({'success': True, 'error_message': None})
        else:
            return JsonResponse({'success': False, 'error_message': 'You already have an order.'})

    else:
        return redirect(home, permanent=True)

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
