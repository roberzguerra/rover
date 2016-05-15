# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template.loader import get_template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django import template

register = template.Library()


@register.filter
def text(value):
    """
    Remove tags e retorna texto seguro
    """
    return mark_safe(strip_tags(value))


@register.filter
def crop_text(text, value):
    """
    Corta texto e add os 2 pontos (...) no final
    """
    result = text
    if len(result) > value:
        result = u"%s..." % result[:value]

    return result


@register.filter
def get_class_name(value):
    return value.__class__.__name__

@register.filter
def get_key(dic, value):
    return dic[value]