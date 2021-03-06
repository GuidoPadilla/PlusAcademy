from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('../../pagos/control')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def staff_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page')
    return wrapper_func