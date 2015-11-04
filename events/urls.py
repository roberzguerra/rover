# -*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from events.views import EventHomePageView, EventHomepagePreview

urlpatterns = patterns('',

    url(r'^(?P<url>[\w-]+)/$', EventHomePageView.as_view(), name="event-homepage"),
    url(r'^preview-homepage/(?P<url>[\w-]+)/$', EventHomepagePreview.as_view(),
       name="event-preview"),

)
