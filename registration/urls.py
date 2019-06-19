from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register_form'),
    path('login/', views.signin_view, name='login_form'),
    path('test/', views.test_session_id, name='test'),
    path('logout/', views.logout_view, name='logout'),
    path('select/', views.select_view, name='select'),
    path('setblood/', views.setblood_view, name='setblood'),
    path('getblood/', views.getblood_view, name='getblood'),
    path('seturine/', views.seturine_view, name='seturine'),
    path('geturine/', views.geturine_view, name='geturine'),
    path('setdiabete/', views.setdiabete_view, name='setdiabete'),
    path('getdiabete/', views.getdiabete_view, name='getdiabete'),
    path('index2/', views.index2_view, name='index2'),

]