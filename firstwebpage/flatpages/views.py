from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # если поля заполнены без ошибок
                if (Article.objects.filter(title=form["title"]).exists()):
                    form['errors'] = u"Заголовок должен быть уникальным"
                    return render(request, 'create_post.html', {'form': form})
                else:
                    Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                    return redirect('archive')
            # перейти на страницу поста
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def register(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'password': request.POST["password"], 'name': request.POST["name"], 'email': request.POST["email"],
            'repeatPass': request.POST["repeatPass"]
        }
        # в словаре form будет храниться информация, введенная пользователем
        if form["password"] and form["name"] and form["email"] and form["repeatPass"]:
            # если поля заполнены без ошибок
            if (User.objects.filter(username=form["name"]).exists()):
                form['errors'] = u"Имя пользователя должно быть уникальным"
                return render(request, 'register.html', {'form': form})
            else:
                if (form["password"] != form["repeatPass"]):
                    form['errors'] = u"Пароли не совпадают"
                    return render(request, 'register.html', {'form': form})
                else:
                    User.objects.create_user(username=form["name"], password=form["password"], email=form["email"])
                    return redirect('archive')
        # перейти на страницу поста
        else:
            # если введенные данные некорректны
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'register.html', {})

def log_in(request):
    if request.method == "POST":
        # обработать данные формы, если метод POST
        form = {
            'password': request.POST["password"], 'name': request.POST["name"]
        }
        # в словаре form будет храниться информация, введенная пользователем
        if form["password"] and form["name"]:
            # если поля заполнены без ошибок
            if (User.objects.filter(username=form["name"]).exists()):
                if (User.objects.get(username=form["name"]).check_password(form["password"])):
                    user = authenticate(request, username=form["name"], password=form["password"])
                    if user is not None:
                        login(request, user)
                        return redirect('archive')
                    else:
                        form['errors'] = u"Неверные данные"
                        return render(request, 'login.html', {'form': form})
                else:
                    form['errors'] = u"Неверные данные"
                    return render(request, 'login.html', {'form': form})
            else:
                form['errors'] = u"Неверные данные"
                return render(request, 'login.html', {'form': form})

        # перейти на страницу поста
        else:
            # если введенные данные некорректны
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})
    else:
        # просто вернуть страницу с формой, если метод GET
        return render(request, 'login.html', {})