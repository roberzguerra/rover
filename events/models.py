# -*- coding:utf-8 -*-

import os
from copy import deepcopy

from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
from django.utils.safestring import mark_safe
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User, Group

from mezzanine.core.fields import FileField, RichTextField, OrderField
from mezzanine.core.models import Displayable, CONTENT_STATUS_CHOICES, CONTENT_STATUS_PUBLISHED, CONTENT_STATUS_DRAFT, \
    Orderable, RichText
from mezzanine.core.request import current_request
from mezzanine.utils.models import AdminThumbMixin

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

    code = models.TextField(verbose_name=_(u"Códigos"), blank=True, null=True, help_text=_(u"Insira aqui códigos HTML, CSS ou JS."))

    # event_blocks = models.ManyToManyField("EventBlock", verbose_name=_(u"Equipes"), blank=True,
    #     related_name="people", ) #through="PeoplePersonCategory"

    # programations = models.ManyToManyField("EventProgramation", verbose_name=_(u"Programação"), blank=True,
    #     related_name="programations", ) #through="PeoplePersonCategory"

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

    def get_absolute_url_with_host(self):
        """
        URL para montar a pre-visualizacao do Evento, para quando ainda estivar com STATUS=DRAFT
        """
        return current_request().build_absolute_uri(self.get_absolute_url())

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

    def get_all_blocks_published(self):
        """
        Busca todos os Blocos de Eventos com Status == Publicados
        :return: lista de EventBlock
        """
        return self.eventblock_set.filter(status=CONTENT_STATUS_PUBLISHED).order_by('_order')

    def get_all_programations_published(self):
        """
        Busca todas as Programações de Eventos com Status == Publicados
        :return: lista de EventProgramation
        """
        return self.eventprogramation_set.filter(status=CONTENT_STATUS_PUBLISHED, programation__status=CONTENT_STATUS_PUBLISHED).order_by('_order')

    def get_all_programations_published_by_date_time(self):
        """
        Busca todas as Programações de Eventos com Status == Publicados
        :return: lista de EventProgramation
        """
        # event_programations = self.eventprogramation_set.filter(status=CONTENT_STATUS_PUBLISHED,
        #     programation__status=CONTENT_STATUS_PUBLISHED).order_by('event__eventprogramation__programation__date_time')
        programations = Programation.objects.filter(eventprogramation__event=self.id, eventprogramation__status=CONTENT_STATUS_PUBLISHED,
            status=CONTENT_STATUS_PUBLISHED).order_by('date_time', '-eventprogramation___order')

        list_programations = {}
        list_dates = []
        for programation in programations:
            #programation = event_programation.programation
            date_time = programation.date_time.strftime("%d/%m/%Y")

            if not list_programations.has_key(date_time):
                list_programations[date_time] = []
                list_dates.append(date_time)
            list_programations[date_time].append(programation)

        context = {
            'list_programations': list_programations,
            'list_dates': list_dates
        }

        return context

    def get_code(self):
        return mark_safe(self.code)



# EVENT_BLOCK_TEXT = 1 # Texto comum
# EVENT_BLOCK_MAP = 2 # Local/Mapa (necessario injetar tags do mapa, o JS eh montado automaticamente
# EVENT_BLOCK_TYPE = (
#     (1, _(u"Conteudo Texto/HTML")),
#     (2, _(u"Local/Mapa")),
# )


class Block(Displayable, RichText, AdminThumbMixin):
    """
    Blocos para eventos
    // RichText
      title
      content
      status
    // Displayable
      publish_date
      expiry_date
      short_url
      in_sitemap

    Tipos de Blocos:
    EVENT_BLOCK_TEXT = 1 # Texto comum
    EVENT_BLOCK_MAP = 2 # Local/Mapa (necessario injetar tags do mapa, o JS eh montado automaticamente
        // Tags para usar MAPAS, Nesta tag sera construido o mapa
        <div class="address-map" data-address="Nome do local (no google maps) ou Latitude, Longitude"></div>
        Exemplo:
        <div class="address-map" data-address="Avenida Senador Salgado Filho, 2785 - Viamão"></div>
    """

    # link_menu = models.IntegerField(_(u"Exibir no Menu"), choices=CHOICE_ACTIVE, default=CONTENT_STATUS_PUBLISHED,
    #     help_text=_(u"Se marcado exibe como link no menu principal."))

    #local_maps_name = models.CharField(verbose_name=_(u"Local no Maps"), max_length=500, blank=True, help_text=_(u"Nome do Local no Google Maps, ou (Latitude, Longitude)."))

    class Meta:
        ordering = ["status", 'pk']
        db_table = "event_block"
        verbose_name = _(u"Bloco para Evento")
        verbose_name_plural = _(u"Blocos para Eventos")

    def __unicode__(self):
        return unicode(self.title)

    def is_published(self):
        """
        :return: True se status == 2 (Publicado)
        """
        if self.status == CONTENT_STATUS_PUBLISHED:
            return True
        return False

    def get_content(self):
        return mark_safe(self.content)


EVENT_BLOCK_TYPE_CONTENT = 1
EVENT_BLOCK_TYPE_PROGRAMATION = 2
EVENT_TYPE_CHOICES = (
    (EVENT_BLOCK_TYPE_CONTENT, _(u"Conteúdo")),
    (EVENT_BLOCK_TYPE_PROGRAMATION, _(u"Programação")),
)


class EventBlock(Orderable):
    """
    Model de ligação dos blocos com Eventos
    """

    event = models.ForeignKey(verbose_name=_(u"Evento"), to=Event, null=True, blank=True, help_text=_(u"Selecione o Evento deste Bloco."))
    # Bloco para montar o select com autocomplete
    block = models.ForeignKey(verbose_name=_(u"Bloco"), to=Block, null=True, blank=True, help_text=_(u"Selecione o Evento deste Bloco."))
    type = status = models.IntegerField(_(u"Tipo"), choices=EVENT_TYPE_CHOICES, default=EVENT_BLOCK_TYPE_CONTENT,
        help_text=_(u"Selecione Programação para exibir as programações do evento."))
    status = models.IntegerField(_("Status"), choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED,
        help_text=_(u"With Draft chosen, will only be shown for admin users on the site."))

    link_menu = models.IntegerField(_(u"Exibir no Menu"), choices=CHOICE_ACTIVE, default=CONTENT_STATUS_PUBLISHED,
        help_text=_(u"Se marcado exibe como link no menu principal."))

    class Meta:
        ordering = ["status", 'pk']
        db_table = "event_eventblock"
        verbose_name = _(u"Bloco de Evento")
        verbose_name_plural = _(u"Blocos de Eventos")

    # def __unicode__(self):
    #     return unicode(self.title)

    def is_published(self):
        """
        :return: True se status == 2 (Publicado)
        """
        if (self.status == CONTENT_STATUS_PUBLISHED):
            return True
        return False

    def show_link_menu(self):
        """
        :return: True se status == 2 (Publicado)
        """
        if (self.link_menu == CONTENT_STATUS_PUBLISHED):
            return True
        return False

    def is_type_content(self):
        """
        :return: True se status == 2 (Publicado)
        """
        if (self.type == EVENT_BLOCK_TYPE_CONTENT):
            return True
        return False

    def is_type_programation(self):
        """
        :return: True se status == 2 (Publicado)
        """
        if (self.type == EVENT_BLOCK_TYPE_PROGRAMATION):
            return True
        return False



class Programation(Displayable, RichText, AdminThumbMixin):
    """
    Programação do Evento
    """
    EVENT_PROGRAMATION_IMAGE_PATH = os.path.join('eventos', 'programacao')
    #status = models.IntegerField(_("Status"), choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED,
    #    help_text=_(u"With Draft chosen, will only be shown for admin users on the site."))
    name = models.CharField(verbose_name=_(u"Nome"), max_length=100, null=False)
    image = FileField(verbose_name=_(u"Imagem"), upload_to=EVENT_PROGRAMATION_IMAGE_PATH, max_length=200, blank=True, null=True,
                      help_text=_(u"Para não distorcer, envie uma imagem com resolução máxima de 200x200px."))
    date_time = models.DateTimeField(verbose_name=_(u"Data e Hora"), help_text=_(u"Data e hora da realização do programa."))

    class Meta:
        ordering = ["-date_time", "-name"]
        db_table = "event_programation"
        verbose_name = _(u"Programação")
        verbose_name_plural = _(u"Programações")

    def __unicode__(self):
        return "%s - %s" % (self.title, self.date_time.strftime("%d/%m/%Y %H:%M:%S"))


class EventProgramation(Orderable):
    """
    Model de ligação das Programações com Eventos
    """

    event = models.ForeignKey(verbose_name=_(u"Evento"), to=Event, null=True, blank=True, help_text=_(u"Selecione o Evento deste Bloco."))
    # Programation para montar o select com autocomplete
    programation = models.ForeignKey(verbose_name=_(u"Programação"), to=Programation, null=True, blank=True, help_text=_(u"Selecione a Programação deste Bloco."))

    status = models.IntegerField(_("Status"),
        choices=CONTENT_STATUS_CHOICES, default=CONTENT_STATUS_PUBLISHED,
        help_text=_(u"With Draft chosen, will only be shown for admin users on the site."))

    link_menu = models.IntegerField(_(u"Exibir no Menu"), choices=CHOICE_ACTIVE, default=CONTENT_STATUS_PUBLISHED,
        help_text=_(u"Se marcado exibe como link no menu principal."))

    class Meta:
        ordering = ["status", 'pk']
        db_table = "event_eventprogramation"
        verbose_name = _(u"Programação")
        verbose_name_plural = _(u"Programações")

    # def __unicode__(self):
    #     return unicode(self.title)

    def is_published(self):
        """
        :return: True se status == 2 (Publicado)
        """
        if (self.status == CONTENT_STATUS_PUBLISHED):
            return True
        return False
