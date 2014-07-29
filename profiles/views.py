from django.shortcuts import render, Http404
from django.contrib.auth.models import User

# Hard code food data model
a = 'WALG(NICE) CHOC CVRD PRTZLS'
b = 'NICE! FRUIT SNACK'
c = 'NESTLE RAISINETS'
d = 'MARS M&M M/CHOC PRTZL SNGL'
e = 'HERSHEY TXZLRS STRWBRY TWST'
f = 'NICE! CORN NUGGETS'
g = 'NICE! XL RSTD/SLTD PEANUTS'
h = 'MARS SNICKERS BAR 42431'
i = 'NAB MINI OREOS'
j = 'NICE! NATURAL ALMONDS'

carb_data = [63, 72, 32, 24, 56, 63, 8, 33, 62, 9]
fat_data = [18, 8, 4.5, 1, 10.5, 21, 12, 17, 22]
protein_data = [6, 3, 2, 2, 2, 6, 11, 4, 4, 9]
sugar_data = [30, 48, 28, 17, 29, 0, 2, 27, 34, 2]
fiber_data = [3, 0, 1, 1, 0, 12, 3, 1, 2, 5]

Recm_data = [300, 65, 50, 36, 25]

# Create your views here.



def home(request):
    return render(request, 'home.html', locals())


def all_users(request):
    users = User.objects.filter(is_active=True)

    return render(request, 'all_users.html', locals())


def user_profile(request, username):
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'single_user.html', locals())


def image_upload(request, username):
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'upload_image.html', locals())


def receipt_tips(request):
    return render(request, 'receipt_tips.html', locals())


def dashboard(request, username):

    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'dashboard.html', locals())


def sugar_dashboard(request, username):

    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'sugar_dashboard.html', locals())


def trend_dashboard(request, username):

    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'trend_dashboard.html', locals())


def recm_dashboard(request, username):

    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'recm_dashboard.html', locals())


def detailed_data(request, username):

    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
    except:
        raise Http404
    return render(request, 'detailed_data.html', locals())








