from django.contrib import admin
from django.urls import path

app_name = 'users'

from users.views import login, register, logout, profile
#
urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]