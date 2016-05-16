# -*- coding:utf-8 -*-
from copy import deepcopy

from django.db.models import Q
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin

from ajax_select.admin import AjaxSelectAdminTabularInline
from ajax_select.fields import autoselect_fields_check_can_add
from events.forms import EventForm, \
    BlockForm, \
    EventBlockInlineForm, \
    ProgramationForm, \
    EventProgramationInlineForm
from events.models import Event, Block, EventBlock, Programation, EventProgramation

from ajax_select import register, LookupChannel

@register('event_blocks')
class EventBlockLookup(LookupChannel):
    """
    Lookup para EventBlock
    """
    model = Block

    def get_query(self, q, request):
        teste
        return self.model.objects.filter(title__icontains=q)


    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % item.title

@register('event_programations')
class EventProgramationLookup(LookupChannel):
    """
    Lookup para EventProgramation
    """
    model = Programation

    def get_query(self, q, request):
        return self.model.objects.filter(Q(title__icontains=q) | Q(date_time__icontains=q))

    def format_item_display(self, item):
        return u"<span class='tag'>%s</span>" % (item)


programation_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
programation_fieldsets[0][1]["fields"].extend(['date_time','image','content'])
programation_list_display = ["title", "status", "description", "events_using"] # "admin_link"]

class ProgramationAdmin(DisplayableAdmin):
    """
    Admin dos Eventos
    """
    form = ProgramationForm
    fieldsets = programation_fieldsets
    list_display = programation_list_display

    # def link_event_change(self, obj):
    #     html = u' - '
    #     if obj.event:
    #         html = u'<a href="%s">%s</a>' % (obj.event.get_admin_url(), obj.event)
    #     return html
    # link_event_change.allow_tags = True
    # link_event_change.short_description = _(u"Evento")

    def get_form(self, request, obj=None, **kwargs):
        form = super(ProgramationAdmin, self).get_form(request, obj, **kwargs)
        autoselect_fields_check_can_add(form, self.model, request.user)
        return form

    def events_using(self, obj):
        """
        monta um link com os eventos utilizando a programação
        :param obj:
        :return:
        """
        html = ''
        event_programations = obj.eventprogramation_set.all()
        event_ids = []
        for event_programation in event_programations:
            event_ids.append(event_programation.event.id)
        if event_ids:
            events = Event.objects.filter(id__in=event_ids)
            for event in events:
                html += "<a href=\"%s\">%s</a>, " % (event.get_admin_url(), event)
        return mark_safe(html)
    events_using.allow_tags = True
    events_using.short_description = _(u"Utilizando nos eventos")


block_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
block_fieldsets[0][1]["fields"].extend(['content'])
block_list_display = ["title", "status", "description", "events_using"] # "admin_link"]

class BlockAdmin(DisplayableAdmin):
    """
    Admin dos Eventos
    """
    form = BlockForm
    fieldsets = block_fieldsets
    list_display = block_list_display

    # def link_event_change(self, obj):
    #     html = u' - '
    #     if obj.event:
    #         html = u'<a href="%s">%s</a>' % (obj.event.get_admin_url(), obj.event)
    #     return html
    # link_event_change.allow_tags = True
    # link_event_change.short_description = _(u"Evento")

    def get_form(self, request, obj=None, **kwargs):
        form = super(BlockAdmin, self).get_form(request, obj, **kwargs)
        autoselect_fields_check_can_add(form, self.model, request.user)
        return form

    def events_using(self, obj):
        """
        monta um link com os eventos utilizando o Bloco
        :param obj:
        :return:
        """
        html = ''
        event_blocks = obj.eventblock_set.all()
        event_ids = []
        for event_block in event_blocks:
            event_ids.append(event_block.event.id)
        if event_ids:
            events = Event.objects.filter(id__in=event_ids)
            for event in events:
                html += "<a href=\"%s\">%s</a>, " % (event.get_admin_url(), event)
        return mark_safe(html)
    events_using.allow_tags = True
    events_using.short_description = _(u"Utilizando nos eventos")


class EventBlockInline(TabularDynamicInlineAdmin, AjaxSelectAdminTabularInline):
    model = EventBlock
    form = EventBlockInlineForm
    ordering = ('_order',)
    fieldsets = (
        (None, {
            #"fields": ["name", "status", "image", "date_time", "content"],
            "fields": ["block", "type", "link_menu", "status", "_order"],
        }),
    )

    # Teste de personalizacao do Admin
    template = "admin/includes/event_dynamic_inline_tabular.html"

    def get_form(self, request, obj=None, **kwargs):
      form = super(EventBlockInline, self).get_form(request, obj, **kwargs)
      autoselect_fields_check_can_add(form, self.model, request.user)
      return form


class EventProgramationInline(TabularDynamicInlineAdmin, AjaxSelectAdminTabularInline):
    model = EventProgramation
    form = EventProgramationInlineForm
    ordering = ('_order',)
    fieldsets = (
        (None, {
            #"fields": ["name", "status", "image", "date_time", "content"],
            "fields": ["programation", "status", "_order"],
        }),
    )

    # Teste de personalizacao do Admin
    template = "admin/includes/event_dynamic_inline_tabular.html"

    def get_form(self, request, obj=None, **kwargs):
      form = super(EventBlockInline, self).get_form(request, obj, **kwargs)
      autoselect_fields_check_can_add(form, self.model, request.user)
      return form


event_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
event_fieldsets[0][1]["fields"].extend([
    'event_title_menu','event_description_short', 'event_logo', 'event_title', 'event_image_background',
    'event_social_image', 'code',
])

event_list_display = ["title", "status", "preview_link"]

class EventAdmin(DisplayableAdmin):
    """
    Admin dos Eventos
    """
    form = EventForm

    fieldsets = event_fieldsets
    list_display = event_list_display
    #filter_horizontal = ("categories",)
    inlines = [
        EventBlockInline,
        EventProgramationInline,
    ]

    def get_form(self, request, obj=None, **kwargs):
      form = super(EventAdmin, self).get_form(request, obj, **kwargs)
      autoselect_fields_check_can_add(form, self.model, request.user)
      return form

    def preview_link(self, obj):
        return u'<a target="_blank" href="%s">%s</a>' % (reverse('events:event-preview', args=(obj.slug,)), _(u"Pré-visualizar"))
    preview_link.allow_tags = True
    preview_link.short_description = _(u"Pré-visualizar")


admin.site.register(Event, EventAdmin)
admin.site.register(Block, BlockAdmin)
admin.site.register(Programation, ProgramationAdmin)