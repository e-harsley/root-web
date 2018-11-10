from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def home(request):
    return render(request, 'courier/index.html', {'section': 'home'})

#def track_order(request):
#    return render(request)

def services(request):
    return render(request, 'courier/service.html', {'section': 'service'})


def about(request):
    return render(request, 'courier/about.html', {'section':'about'})

def contact(request):
    return render(request, "courier/contact.html", {'section':'contact'})

@login_required
def waybillform(request):
    if request.method == 'POST':
        user_form = WaybillForms(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request,
                          'courier/index.html',
                          {'new_user': new_user})
    else:
        user_form = WaybillForms()
    return render(request, 'courier/form.html', {'user_form': user_form})

@login_required
def courier_profile(request):
    users = request.user
    goods = Waybill.objects.filter(user=users)
    return render(request, 'courier/profile.html',{'goods':goods}, {'section': 'profile'})

@login_required
def goods_detail(request, id):
    courier = get_object_or_404(Waybill, id=id)
    return render(request,
                  'courier/detail.html',
                  {'section': 'profile',
                   'courier': courier,})