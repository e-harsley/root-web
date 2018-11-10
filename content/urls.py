from django.urls import path
from . import views
from django.contrib.auth import login
urlpatterns = [
    path('home/', views.home, name="home"),
    #path('track-order', ),
    path('services', views.services, name="service"),
    path('shipping-form', views.services, name="shipping-form"),
    path('about',  views.about, name="about"),
    path('profile',  views.courier_profile, name="profile"),
    path('contact', views.contact, name="contact"),
    path('detail/<int:id>/', views.goods_detail, name='detail'),
    path("login", login, name="login"),
]