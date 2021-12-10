from django.urls import path
from . import views

# 기본 url = 'main/'
urlpatterns = [
    path('',views.signUp),
    path('login/',views.login),
    path('logout/',views.logout)
]