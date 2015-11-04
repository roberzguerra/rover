# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class InstitutionalConfig(AppConfig):
    name = 'institutional'
    verbose_name = _(u"Institucional")
