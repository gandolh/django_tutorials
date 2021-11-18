from django.urls import path
from . import views

#url configuration
urlpatterns = [
    path('hello/', views.say_Hello )
]