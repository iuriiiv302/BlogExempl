from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf

from .forms import CommentForm
from .models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.contrib import auth

def articles(request):
    return render_to_response('exemple/articles.html', {'articles': Article.objects.all(), 'username':auth.get_user(request).username}) # отправлем пользователя из сесии в шаблон


def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username

def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id)  # Проверка существует ли статься
        article.article_likes += 1
        article.save()
        response = redirect('http://127.0.0.1:8000/articles/all/')
        response.set_cookie(article_id,"test")
        return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('http://127.0.0.1:8000/articles/all/')


def addcomment(request, article_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # получаем коментарий из формы
            comment.comments_article = Article.objects.get(id=article_id)  # поиск нужного поста
            form.save()
    return redirect('http://127.0.0.1:8000/articles/get/%s/' % article_id)
