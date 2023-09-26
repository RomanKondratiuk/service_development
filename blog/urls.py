from django.urls import path
from . import views

urlpatterns = [
    path('blog/articles/', views.blog_articles, name='blog_articles'),
    path('article/<int:pk>/', views.blog_article_detail, name='blog_article_detail'),
    # ...
]
