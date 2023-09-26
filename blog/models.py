from django.db import models
from django.utils import timezone


class BlogArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    content = models.TextField(verbose_name='content')
    image = models.ImageField(upload_to='media/', verbose_name='image')
    views = models.PositiveIntegerField(default=0, verbose_name='views')
    pub_date = models.DateTimeField(default=timezone.now, verbose_name='date_of_publication')

    def __str__(self):
        return self.title
