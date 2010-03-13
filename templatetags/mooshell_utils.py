from django import template
from django.utils import simplejson
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def jsonify_pasties(pasties, server):
    """
        returns json version of pasties.
    """    
    def build_dict(pastie):
        shell = pastie.favourite
        return {
            "title": shell.title,
            "author": shell.author.username,
            "description": shell.description,
            "url": "%s%s" % (server, shell.get_absolute_url()),
            "version": shell.version,
            "created": shell.created_at.strftime("%Y-%m-%d %H:%I:%S"),
            "framework": shell.js_lib.library_group.name
        }
    
    return mark_safe(simplejson.dumps([build_dict(pastie) for pastie in pasties]))
