from django.shortcuts import render
from django.http import HttpResponse

def home(request):
#   return HttpResponse(u'Привет, Мир!', content_type="text/plain")
    return render(request, 'templates/static_handler.html')

def hello(request):
    return u'Привет, Мир!'
