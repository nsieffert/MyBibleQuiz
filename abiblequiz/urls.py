from django.urls import path
from . import views # we are importing the views.py file

urlpatterns = [
    path('setup', views.setup, name='setup'),  # Make the setup screen the default home page!
    path('index', views.index, name='index')] # Move the actual game to /game/