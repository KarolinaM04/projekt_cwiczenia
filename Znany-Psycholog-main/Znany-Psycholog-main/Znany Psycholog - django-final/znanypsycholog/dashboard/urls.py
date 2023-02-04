from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('main_view', views.main_view),
    path('', views.index, name='index'),
    path('login-page/', views.login_page, name='login_page'),
    path('after-page/', views.after_login, name='after_login'),
    path('forum/', views.forum, name='forum'),
]
