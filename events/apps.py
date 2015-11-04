# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class EventsConfig(AppConfig):
    name = 'events'
    verbose_name = _(u"Eventos")
