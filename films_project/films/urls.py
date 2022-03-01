# films/urls.py
from django.urls import path
from . import views

app_name = 'films'
urlpatterns = [
    path('', views.main, name='main'),
    path('user_info/', views.user_info, name='user_info'),
    ## new route below ##
    path('user_form/', views.user_form, name= 'user_form'),
    #new notation <int:id>. the < > signs here show we are dealing with a new parameter type called route parameter
    #int shows that it is an object from the int class and id tells Django that a primary key is expected here.
    path('<int:id>/details', views.details, name='details'),
]