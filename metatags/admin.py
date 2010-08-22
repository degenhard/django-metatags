from django.contrib.contenttypes import generic
from models import MetaTag

class MetaTagInline(generic.GenericStackedInline):
    model = MetaTag
    extra = 1
    max_num = 1
    ct_field = 'content_type'
    ct_fk_field = 'object_id'
    
    class Media:
        css = {
            'screen': ('metatags/metatags.css',)
        }
        js = ('metatags/metatags.js',)