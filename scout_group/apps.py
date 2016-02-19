# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class ScoutGroupConfig(AppConfig):
    name = 'scout_group'
    verbose_name = _(u"Grupos | Distritos")
