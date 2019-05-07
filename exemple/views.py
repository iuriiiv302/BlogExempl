from django.shortcuts import render_to_response
from .models import Article, Comments


def articles(request):
    return render_to_response('exemple/articles.html', {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response('exemple/article.html', {'article': Article.objects.get(id=article_id),
                                               'comments': Comments.objects.filter(comments_article_id=article_id)})
