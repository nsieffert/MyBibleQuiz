from django.urls import path
from . import views # we are importing the views.py file

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz_load', views.quiz_load, name='quiz_load')]