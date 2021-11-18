from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#pull data from db
#Transform
#send Email

def say_Hello( request):
    return render(request,'hello.html',{'team_name':'UV_TEAM'},content_type='text/html')
 