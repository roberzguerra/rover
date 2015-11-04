# -*- coding:utf-8 -*-
from copy import deepcopy
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import Displayable, CONTENT_STATUS_CHOICES, CONTENT_STATUS_PUBLISHED, CONTENT_STATUS_DRAFT
from mezzanine.core.models import RichText
from mezzanine.utils.models import AdminThumbMixin
import os

from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.conf import settings

from django.utils.translation import ugettext_lazy as _
from django.db import models

from django.contrib.auth.models import User, Group

#from core.models import CoreModel, ACTIVE, INACTIVE, CHOICE_ACTIVE


ACTIVE = CONTENT_STATUS_PUBLISHED # 2
INACTIVE = CONTENT_STATUS_DRAFT # 1
CHOICE_ACTIVE = (
    (CONTENT_STATUS_PUBLISHED, _(u"Sim")),
    (CONTENT_STATUS_DRAFT, _(u"Não")),
)

class Event(Displayable, RichText, AdminThumbMixin):
    """
    Evento
    """
    EVENT_IMAGE_PATH = os.path.join('eventos','evento')

    event_title_menu = models.CharField(verbose_name=_(u"Título do Evento para o Menu"), max_length=255, blank=False,
        null=False, help_text=_(u"Título que vai no link à esquerda no Menu do Topo. Máximo 255 caracteres. Ex: Congresso"))
    event_description_short = models.CharField(verbose_name=_(u"Descrição curta"), max_length=255, blank=False,
        null=False, help_text=_(u"Descrição curta para Buscadores e Redes sociais. Ex: Congresso Escoteiro Regional 2015"))
    # event_url = models.SlugField(verbose_name=_(u"Nome da URL do Evento"), unique=True, max_length=255, blank=False,
    #                              null=False, help_text=_(u"Nome do link, ex: congresso-2015"))

    # Cabecalho
    event_logo = FileField(verbose_name=_(u"Cabeçalho Logo"), upload_to=EVENT_IMAGE_PATH, format="Image", max_length=255, null=True, blank=True)
    #event_title = RichTextField(verbose_name=_(u"Cabeçalho Título"), blank=True, config_name='description')
    event_title = RichTextField(verbose_name=_(u"Cabeçalho Título"), blank=True, default='',
        help_text=_("This field can contain HTML and should contain a few paragraphs describing the background of the person."),)
    event_image_background = FileField(verbose_name=_(u"Cabeçalho Imagem de Fundo"), upload_to=EVENT_IMAGE_PATH, max_length=200, blank=True, null=True,
        help_text=_(u"Para não distorcer, envie uma imagem com resolução máxima de 2362x591px."))
    event_social_image = FileField(verbose_name=_(u"Imagem para Redes Sociais"), upload_to=EVENT_IMAGE_PATH, max_length=200, blank=True, null=True,
        help_text=_(u"Imagem para exibir em links de Redes Sociais, como Facebook. Para imagem retangular envie em 600x315, para imagem quadrada envie em 200x200. Ou formatos maiores sempre mantendo a proporção."))

    # Informacoes
    information_active = models.IntegerField(verbose_name=_(u"Exibir Bloco Informações"), choices=CHOICE_ACTIVE, default=INACTIVE, blank=False)
    information_title = RichTextField(verbose_name=_(u"Informações Título"), null=True, blank=True)
    information_text = RichTextField(verbose_name=_(u"Informações Texto"), null=True, blank=True)

    # LOCAL
    local_active = models.IntegerField(verbose_name=_(u"Exibir Bloco Local"), choices=CHOICE_ACTIVE, default=INACTIVE, blank=False)
    local_maps_name = models.CharField(verbose_name=_(u"Local no Maps"), max_length=500, blank=True, help_text=_(u"Nome do Local no Google Maps."))
    local_title = RichTextField(verbose_name=_(u"Local Título"), null=True, blank=True)
    local_text = RichTextField(verbose_name=_(u"Local Texto"), blank=True,)

    # Observacoes
    observation_active = models.IntegerField(verbose_name=_(u"Exibir Bloco Observações"), choices=CHOICE_ACTIVE, default=INACTIVE, blank=False)
    observation_title = RichTextField(verbose_name=_(u"Observações Título"), null=True, blank=True)
    observation_text = RichTextField(verbose_name=_(u"Observações Texto"), blank=True,)

    # Lista de Programacao
    list_programations_active = models.IntegerField(verbose_name=_(u"Ativar Lista de Programações"), max_length=1, choices=CHOICE_ACTIVE, default=INACTIVE, blank=False)
    list_programations_title = RichTextField(verbose_name=_(u"Lista de Programações Título"), blank=True)

    # Lista de Eventos
    list_events_active = models.IntegerField(verbose_name=_(u"Ativar Lista de Eventos"), max_length=1, choices=CHOICE_ACTIVE, default=INACTIVE, blank=False)
    list_events_title = RichTextField(verbose_name=_(u"Lista de Eventos Título"), null=True, blank=True)

    class Meta:
        ordering = ["status", 'pk']
        db_table = "event_homepage"
        verbose_name = _(u"Evento")
        verbose_name_plural = _(u"Eventos")

    def __unicode__(self):
        """
        text = strip_tags(self.event_title)
        if len(text) > 50:
            text = "%s..." % text[0:50]
        else:
            text = "%s" % text
        return mark_safe(text)
        """
        return unicode(self.title)

    def get_text(valor):
        return mark_safe(strip_tags(valor))

    def get_absolute_url(self):
        """
        URL absoluta do Evento
        """
        return reverse('events:event-homepage', args=(self.slug,))

    def get_url_preview(self):
        return reverse('events:event-preview', args=(self.slug,))

    def get_link_preview(self):
        return '<a href="%s" target="_blank">%s</a>' % (
            reverse('events:event-preview', args=(self.slug,)), unicode(_(u"Pré-visualizar")))

    def duplicate_save(self):
        obj_new = deepcopy(self)
        obj_new.id = None
        obj_new.title += "Cópia de %s" % (obj_new.title)
        obj_new.homepage_active = INACTIVE
        obj_new.save()
        return obj_new

    def is_information_active(self):
        if self.information_active == ACTIVE:
            return True
        else:
            return False

    def is_local_active(self):
        if self.local_active == ACTIVE:
            return True
        else:
            return False

    def is_observation_active(self):
        if self.observation_active == ACTIVE:
            return True
        else:
            return False

    def is_list_programations_active(self):
        if self.list_programations_active == ACTIVE:
            return True
        else:
            return False

    def get_event_logo(self):
        """
            retorna o caminho do logo do evento para montar a URL
        """
        if self.event_logo:
            return "%s/%s" % (settings.MEDIA_URL, self.event_logo)
        else:
            return False

    def get_event_image_background(self):
        if self.event_image_background:
            return "%s/%s" % (settings.MEDIA_URL, self.event_image_background)
        else:
            return os.path.join(settings.STATIC_URL, 'events', 'img', 'header.jpg')

    def get_event_social_image(self):
        """
            retorna o caminho do logo do evento para montar a URL
        """
        if self.event_logo:
            return "%s/%s" % (settings.MEDIA_URL, self.event_social_image)
        else:
            return ''

    def get_programation_list(self):
        """
        Busca apenas as programacoes ATIVAS do evento
        """
        return self.eventprogramation_set.filter(status=ACTIVE).order_by('date_time')


class EventProgramation(RichText, AdminThumbMixin):
    """
    Programação do Evento
    """
    EVENT_PROGRAMATION_IMAGE_PATH = os.path.join('eventos', 'programacao')
    status = models.IntegerField(_("Status"),
        choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED,
        help_text=_(u"With Draft chosen, will only be shown for admin users on the site."))
    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    image = FileField(verbose_name=_(u"Imagem"), upload_to=EVENT_PROGRAMATION_IMAGE_PATH, max_length=200, blank=True, null=True,
                      help_text=_(u"Para não distorcer, envie uma imagem com resolução máxima de 200x200px."))
    date_time = models.DateTimeField(verbose_name=_(u"Data e Hora"))

    # Conteudo: jaesta no model RichText como content
    #description = RichTextField(verbose_name=_(u"Descrição"), blank=True)
    event = models.ForeignKey(verbose_name=_(u"Evento"), to=Event, null=True, blank=True, help_text=_(u"Selecione o Evento desta Programação."))

    class Meta:
        ordering = ["-date_time", "-name"]
        db_table = "event_programation"
        verbose_name = _(u"Programação")
        verbose_name_plural = _(u"Programações")

    def __unicode__(self):
        return "%s - %s" % (self.name, self.date_time)

