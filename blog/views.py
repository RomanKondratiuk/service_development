from django.shortcuts import render, get_object_or_404

from blog.models import BlogArticle


def blog_articles(request):
    articles = BlogArticle.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'blog/articles.html', context)


def blog_article_detail(request, pk):
    article = get_object_or_404(BlogArticle, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})
