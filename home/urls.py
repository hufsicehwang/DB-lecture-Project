from django.urls import path
from . import views

# 기본 url = 'home/'
urlpatterns = [
    path('dbtest/',views.data_insert, name='data_insert'),
    path('review/',views.review, name='home'),
    path('search/',views.searchMovie),
    path('',views.home),
    path('mylist/',views.mylist),
    path('list/',views.list),
    path('detail/<str:name>',views.detail),
]