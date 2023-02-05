from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('user/',views.user_register,name='sign-up'),
    path('add-ques/',views.ques_add,name='ques-add'),
    path('login/',auth_views.LoginView,name='login'),
]
