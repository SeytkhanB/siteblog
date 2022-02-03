
from django import template
from blog.models import Post, Tag

# register = template.Library       # due to I didn't take brackets I had en error
register = template.Library()

@register.inclusion_tag('blog/popular_posts_tpl.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by('-numbers_of_views')[:cnt]
    return {'posts': posts}

@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {'tags': tags}

