# -*- coding:utf-8 -*-
from copy import deepcopy

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin
from events.forms import EventForm, EventProgramationForm
from events.models import Event, EventProgramation



class EventProgramationInline(TabularDynamicInlineAdmin):
    model = EventProgramation
    #form = EventProgramationForm
    fieldsets = (
        (None, {
            "fields": ["name", "status", "image", "date_time", "content"],
        }),
    )


event_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
event_fieldsets[0][1]["fields"].extend([
    'event_title_menu','event_description_short',
    'event_logo', 'event_title', 'event_image_background', 'event_social_image',
    'information_active', 'information_title', 'information_text',
    'local_active', 'local_maps_name', 'local_title', 'local_text',
    'observation_active', 'observation_title', 'observation_text',
    'list_programations_active', 'list_programations_title',
    'list_events_active', 'list_events_title',
])

event_list_display = ["title", "status", "admin_link"]


class EventAdmin(DisplayableAdmin):
    """
    Admin dos Eventos
    """
    form = EventForm
    fieldsets = event_fieldsets
    list_display = event_list_display
    #filter_horizontal = ("categories",)
    inlines = [
        EventProgramationInline,
    ]


class EventProgramationAdmin(admin.ModelAdmin):
    """
    Admin das Programacoes de Eventos
    """
    form = EventProgramationForm
    fieldsets = (
        (None, {
            "fields": ["name", "status", "image", "date_time", "content", "event",],
        }),
    )
    list_display = ["name", "status", "link_event_change"]
    list_display_links = ['name',]
    ordering = ('date_time', 'name', 'status', 'content')
    list_filter = (
        ('status', admin.ChoicesFieldListFilter),
        'event',
    )

    def link_event_change(self, obj):
        html = u' - '
        if obj.event:
            html = u'<a href="%s">%s</a>' % (obj.event.get_admin_url(), obj.event)
        return html

    link_event_change.allow_tags = True
    link_event_change.short_description = _(u"Evento")

admin.site.register(Event, EventAdmin)
admin.site.register(EventProgramation, EventProgramationAdmin)