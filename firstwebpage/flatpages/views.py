from django.shortcuts import render
from django.http import HttpResponse
from .models import Article

def home(request):
#   return HttpResponse(u'Привет, Мир!', content_type="text/plain")
    return render(request, 'templates/static_handler.html')

def hello(request):
    return HttpResponse(u'Привет, Мир!')

def archive(request):
    return render(request, 'templates/archive.html', {"posts": Article.objects.all()})
