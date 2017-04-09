# -*- coding: utf-8 -*-

from django import template
from django.core.exceptions import ImproperlyConfigured

from classytags.core import Options
from classytags.helpers import InclusionTag
from classytags.arguments import Argument, IntegerArgument

from ..conf import settings


class MapTag(InclusionTag):
    """
    The syntax:

    {% map <lat> <lng> [<width> <height> <zoom>] %}

    """
    name = 'map'
    template = 'easy_maps/map.html'
    options = Options(
        Argument('lat', resolve=True, required=True),
        Argument('lng', resolve=True, required=True),
        IntegerArgument('width', required=False, default=320),
        IntegerArgument('height', required=False, default=240),
        IntegerArgument('zoom', required=False, default=18),
        'using',
        Argument('template_name', default=None, required=False),
    )

    def render_tag(self, context, **kwargs):
        if settings.EASY_MAPS_GOOGLE_MAPS_API_KEY is None:
            raise ImproperlyConfigured(
                "easy_map tag requires EASY_MAPS_GOOGLE_MAPS_API_KEY to be "
                "set in global settings because of the restrictions "
                "introduced in Google Maps API v3 by Google, Inc."
            )

        return super(MapTag, self).render_tag(context, **kwargs)

    def get_template(self, context, **kwargs):
        return kwargs.get('template_name', None) or self.template

    def get_context(self, context, **kwargs):
        kwargs['api_key'] = settings.EASY_MAPS_GOOGLE_MAPS_API_KEY

        return kwargs


register = template.Library()
register.tag(MapTag)
