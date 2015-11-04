# -*- coding:utf-8 -*-
from django.template.defaultfilters import safe

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
#from core.models import ACTIVE
from mezzanine.core.fields import RichTextField
from events.models import Event, EventProgramation
#from bootstrap_admin.widgets import LinkButton


class EventForm(ModelForm):
    """
    Form para o Evento
    """

    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(EventForm, self).__init__(*args, **kwargs)
        css_class = {'class': 'simple'}
        self.fields['information_title'].widget.attrs.update(css_class)
        self.fields['local_title'].widget.attrs.update(css_class)
        self.fields['observation_title'].widget.attrs.update(css_class)
        self.fields['list_programations_title'].widget.attrs.update(css_class)
        self.fields['list_events_title'].widget.attrs.update(css_class)


    def clean(self):
        # homepage_active = self.cleaned_data.get('homepage_active')
        # if homepage_active == ACTIVE and self.instance.has_more_one_active():
        # self.add_error('homepage_active', safe(_(u"Apenas um registro pode estar Ativo, deixe o campo <strong>Inativo</strong>.")))

        return self.cleaned_data


class EventProgramationForm(ModelForm):
    """
    Form para a Programacao do Evento
    """

    class Meta:
        model = EventProgramation
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(EventProgramationForm, self).__init__(*args, **kwargs)