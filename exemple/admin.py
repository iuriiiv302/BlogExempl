from django.contrib import admin

from .models import Article, Comments


class ArticleInLine(admin.StackedInline):
    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date']
    inlines = [ArticleInLine]


admin.site.register(Article, ArticleAdmin)

# admin.site.register(Article)
# admin.site.register(Comments)
