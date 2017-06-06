from django.shortcuts import render
from models import Article

def latest_article(request):
    article_list = Article.objects.order_by('-id')
    return render(request, 'articles.html', {'article_list':article_list})