from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='default'),
    path('about/', views.about , name='about'),
    path('home/', views.home , name='home'),
    path('store/',views.store, name='store'),
]


