from django import template
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache

from metatags import app_settings, models

register = template.Library()

@register.inclusion_tag('metatags/meta_tags.html')
def meta(obj=None, meta={}):
    """
    Template tag to generate meta tags. Takes an optional parameter of a 
    template object to pull the tags from. If not passed, it will return the 
    default meta tags, as set in their respective templates.
    """
    cachename = obj and 'metatags_%s_%s' % (
        obj.__class__.__name__,
        obj.id
    ) or 'meta_default'
    meta_tags = cache.get(cachename)
    if not meta_tags:
        try:
            meta_tags = MetaTag.objects.get(
                content_type=ContentType.objects.get_for_model(obj.__class__),
                object_id=obj.pk
            )
        except (AttributeError, IndexError):
            meta_tags = None
        if app_settings.METATAGS_CACHE_TTL:
            cache.set(cachename, meta_tags, app_settings.METATAGS_CACHE_TTL)
    return { 'meta_tags': meta }