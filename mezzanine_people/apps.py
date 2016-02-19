# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class MezzaninePeopleConfig(AppConfig):
    name = 'mezzanine_people'
    verbose_name = _(u"Equipes")
