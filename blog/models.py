

from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title                                           # gives title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})      # getting absolute url

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']



class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']



class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, verbose_name='Url', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Published')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    numbers_of_views = models.IntegerField(default=0, verbose_name='Numbers of views')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    """if we have written class Category before this line of definition 
    we can write like this       ↑    without quotes 
    if we have written class Category after definition then we should 
    write definition like this   ↓    with quotes
    ategory = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    """

    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created_at']

