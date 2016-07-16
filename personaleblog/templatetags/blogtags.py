from django import template
from personaleblog.models import *
register=template.Library()

@register.inclusion_tag('blog/show_latest.html')
def latest_article(count=5):
    articles=Article.objects.all().order_by('-create_at')[:count]
    return {'articles':articles}