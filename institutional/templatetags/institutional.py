# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.template import Context
from django.template.loader import get_template
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django import template

from mezzanine.conf import settings
from ..models import HomePage

register = template.Library()


@register.simple_tag(takes_context=True)
def get_social_links(context=None, *args, **kwargs):
    """
    Retorna um html renderizado contendo os links de redes sociais da pagina inicial

    **Tag name**::

        get_social_links

    **Parameters**:

        :context:
        :args:
        :kwargs:

    **usage**::

        {% get_social_links %}

    **example**::

        {% get_social_links FIXTHIS %}

    """
    if settings.HOME_PAGE_SITE:
        home = get_object_or_404(HomePage, slug=settings.HOME_PAGE_SITE)
    else:
        home = ''

    context = {'lista_links': home.sociallinks_set.all()}

    temp = get_template('institution/footer_social_links.html')
    return temp.render(Context(context))
    # return get_template('institution/footer_social_links.html').render(Context(context))