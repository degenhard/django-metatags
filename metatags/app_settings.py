from django.conf import settings

METATAGS_CACHE_TTL = getattr(settings, 'META_CACHE_TTL', None)