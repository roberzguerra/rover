# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse, resolve
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED

from events.models import ACTIVE
from events.auth import events_permission_required
from events.models import Event


class EventHomePageView(TemplateView):
    """
    URL: http://g1.globo.com/dynamo/economia/rss2.xml
    """

    template_name = "events/event_homepage.html"
    object = Event
    queryset = []

    def get(self, request, url=None, *args, **kwargs):
        self.slug = url
        return super(EventHomePageView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventHomePageView, self).get_context_data(**kwargs)
        context.update({
            'event': get_object_or_404(Event, slug=self.slug, status=CONTENT_STATUS_PUBLISHED)
            # 'programation_list': Programation.objects.filter(active=ACTIVE).order_by('date_time'),
        })
        return context


class EventHomepagePreview(TemplateView):
    template_name = 'events/event_homepage.html'

    @method_decorator(events_permission_required('events.change_event'))
    def dispatch(self, *args, **kwargs):
        return super(EventHomepagePreview, self).dispatch(*args, **kwargs)

    def get(self, request, url=None, *args, **kwargs):
        self.event_url = url
        return super(EventHomepagePreview, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EventHomepagePreview, self).get_context_data(**kwargs)
        context.update({
            'event': get_object_or_404(Event, event_url=self.event_url)
        })

        return context
