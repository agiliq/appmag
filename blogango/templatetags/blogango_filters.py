import re

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from taggit.models import Tag, TaggedItem
from blogango.views import _get_archive_months
from blogango.models import Blog

register = template.Library()

class BlogangoContext(template.Node):
    def __init__(self):
        pass

    def render(self, context):
        #only one blog must be present
        blog = Blog.objects.get_blog()
        tags = Tag.objects.all()
        tags = [tag for tag in tags if tag.taggit_taggeditem_items.all().count()>2]
        feed_url = reverse('blogango_feed')
        archive_months = _get_archive_months()
        site = Site.objects.get_current()

        extra_context = {
                         'tags': tags,
                         'feed_url': feed_url,
                         'archive_months': archive_months,
                         'blog': blog,
                         'site': site,
                         }
        context.update(extra_context)
        return ''

def blogango_extra_context(parser, token):
    return BlogangoContext()


@register.assignment_tag
def related_posts(post):
    tags = post.tags.all()
    related_posts = TaggedItem.objects.filter(tag__in=tags).filter(
        blogentry__is_published=True).exclude(blogentry=post
        ).distinct().order_by("-blogentry__created_on")[:5]
    return set([el.content_object for el in related_posts])

#django snippets #2107
@register.filter(name='twitterize')
def twitterize(token):
    return re.sub(r'\W(@(\w+))', r'<a href="https://twitter.com/\2">\1</a>', token)
twitterize.is_safe = True

register.tag('blogango_extra_context', blogango_extra_context)

@register.filter
def truncate_chars(ip_string, length=30):
    length, dots = int(length), 3
    if len(ip_string) < length:return ip_string
    else:return ip_string[:length-dots] + '.' * dots
