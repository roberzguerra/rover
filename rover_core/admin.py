# -*- coding:utf-8 -*-

from copy import deepcopy
from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import Page, RichTextPage

page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(3, u"image")
page_fieldsets[0][1]["fields"].insert(4, u"content")


class CorePageAdmin(PageAdmin):
    fieldsets = page_fieldsets

admin.site.unregister(Page)
admin.site.register(Page, CorePageAdmin)

admin.site.unregister(RichTextPage)
admin.site.register(RichTextPage, CorePageAdmin)