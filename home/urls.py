from django.urls import path
from . import views

# 기본 url = 'home/'
urlpatterns = [
    path('review/',views.review, name='home'),
]