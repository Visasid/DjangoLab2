from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404

def home(request):
#   return HttpResponse(u'Привет, Мир!', content_type="text/plain")
    return render(request, 'templates/static_handler.html')

def hello(request):
    return HttpResponse(u'Привет, Мир!')

def archive(request):
    return render(request, 'templates/archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
  try:
    post = Article.objects.get(id=article_id)
    return render(request, 'article.html', {"post": post})
  except Article.DoesNotExist:
    raise Http404
