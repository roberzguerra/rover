# -*- coding:utf-8 -*-
from django.template.defaultfilters import safe

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms import ModelForm
from mezzanine.core.forms import DynamicInlineAdminForm

from events.models import Event, Block, EventBlock, EventProgramation
from ajax_select.fields import AutoCompleteSelectField


class ProgramationForm(ModelForm):
    """
    Form para a Programação
    """
    gen_description = forms.BooleanField(label=_("Generate description"),
        help_text=_("If checked, the description will be automatically "
                    "generated from content. Uncheck if you want to manually "
                    "set a custom description."), required=False, initial=False)
    in_sitemap = forms.BooleanField(label=_(u"Show in sitemap"), required=False, initial=False)

    class Meta:
        model = Block
        fields = '__all__'

    def clean(self):
        # homepage_active = self.cleaned_data.get('homepage_active')
        # if homepage_active == ACTIVE and self.instance.has_more_one_active():
        # self.add_error('homepage_active', safe(_(u"Apenas um registro pode estar Ativo, deixe o campo <strong>Inativo</strong>.")))
        return self.cleaned_data


class BlockForm(ModelForm):
    """
    Form para o Bloco
    """
    gen_description = forms.BooleanField(label=_("Generate description"),
        help_text=_("If checked, the description will be automatically "
                    "generated from content. Uncheck if you want to manually "
                    "set a custom description."), required=False, initial=False)
    in_sitemap = forms.BooleanField(label=_(u"Show in sitemap"), required=False, initial=False)

    class Meta:
        model = Block
        fields = '__all__'

    def clean(self):
        # homepage_active = self.cleaned_data.get('homepage_active')
        # if homepage_active == ACTIVE and self.instance.has_more_one_active():
        # self.add_error('homepage_active', safe(_(u"Apenas um registro pode estar Ativo, deixe o campo <strong>Inativo</strong>.")))
        return self.cleaned_data


class EventProgramationInlineForm(DynamicInlineAdminForm):
    """
    Form para o EventProgramation Inline
    """
    programation = AutoCompleteSelectField('event_programations', required=True, help_text=_(u"Busque pela Programação."),
                                    plugin_options={'url_edit': "/admin/events/programation/"})

    class Meta:
        model = EventProgramation
        fields = '__all__'


class EventBlockInlineForm(DynamicInlineAdminForm):
    """
    Form para o EventBloco Inline
    """
    block = AutoCompleteSelectField('event_blocks', required=True, help_text=_(u"Busque pela Programação."),
                                    plugin_options={'url_edit': "/admin/events/block/"})
    # widget=AutoCompleteSelectMultipleWidget('programations', attrs={'class': 'event_ajax_select'}))

    class Meta:
        model = EventBlock
        fields = '__all__'


class EventForm(ModelForm):
    """
    Form para o Evento
    """

    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        super(EventForm, self).__init__(*args, **kwargs)
        #css_class = {'class': 'simple'}

        #self.fields['information_title'].widget.attrs.update(css_class)
        #self.fields['local_title'].widget.attrs.update(css_class)
        #self.fields['observation_title'].widget.attrs.update(css_class)
        # self.fields['list_programations_title'].widget.attrs.update(css_class)
        # self.fields['list_events_title'].widget.attrs.update(css_class)


    def clean(self):
        # homepage_active = self.cleaned_data.get('homepage_active')
        # if homepage_active == ACTIVE and self.instance.has_more_one_active():
        # self.add_error('homepage_active', safe(_(u"Apenas um registro pode estar Ativo, deixe o campo <strong>Inativo</strong>.")))

        return self.cleaned_data