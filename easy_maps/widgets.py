# -*- coding: utf-8 -*-

from django import template
from django.forms import TextInput
from decimal import *
from civic_map import settings


class AddressWithMapWidget(TextInput):
    width = 700
    height = 200
    zoom = 18

    tpl = (
        '{{%% load easy_maps_tags %%}}'
        '{{%% easy_map address %d %d %d %%}}'
    ) % (width, height, zoom)

    def render(self, name, value, attrs=None):
        output = super(AddressWithMapWidget, self).render(name, value, attrs)

        t = template.Template(self.tpl.format(self))
        context = template.Context({
            'address': value,
        })
        return output + t.render(context)


class MapWidget(TextInput):
    width = 700
    height = 200
    zoom = 18

    tpl = (
        '{{%% load map_tags %%}}'
        '{{%% map lat lng True %d %d %d %%}}'
    ) % (width, height, zoom)

    def render(self, name, value, attrs=None):
        output = super(MapWidget, self).render(name, value, attrs)

        try:
            lat, lng = map(lambda x: Decimal(x.strip()), value.split(','))
        except:
            lat, lng = settings.EASY_MAPS_CENTER

        t = template.Template(self.tpl.format(self))
        context = template.Context({
            'lat': lat,
            'lng': lng,
        })
        return output + t.render(context)
