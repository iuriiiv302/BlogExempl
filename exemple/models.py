from django.db import models


class Article(models.Model):
    class Meta:
        db_table = "article"

    article_title = models.CharField(max_length=250)
    article_text = models.TextField()
    article_date = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = "Comments"
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article, on_delete=models.CASCADE)
