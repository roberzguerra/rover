# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.db import models
from mezzanine.core.fields import RichTextField, FileField
from mezzanine.core.managers import SearchableManager
from mezzanine.core.models import Displayable, RichText, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import AdminThumbMixin

from rover_core.util import UF


class District(Displayable, RichText, AdminThumbMixin):
    """
    Distrito Escoteiro
    """

    name = models.CharField(_(u"Nome"), max_length=500)
    number = models.IntegerField(verbose_name=_(u"Numeral"), null=False, blank=False)
    logo = FileField(verbose_name=_(u"Logo"), upload_to="distritos", format="Image", max_length=255,
                     null=True, blank=True, help_text=_(u'Envie imagens com proporção de 140x140px'))
    coordinator_name = models.CharField(verbose_name=_(u"Coordenador Distrital"), max_length=255)
    email = models.EmailField(blank=True, max_length=255, help_text=_(u'E-mail do distrito ou do coordenador.'))
    uf = models.CharField(verbose_name=_(u"UF"), max_length=2, choices=UF, null=False, blank=False, default=UF[0][0], help_text=_(u"Estado do Distrito."))
    address = models.CharField(verbose_name=_(u"Endereço"), blank=True, max_length=500)
    cep = models.CharField(verbose_name=_(u"CEP"), blank=True, max_length=8)
    image = FileField(verbose_name=_(u"Imagem Destaque"), upload_to="distritos", format="Image", max_length=255,
                     null=True, blank=True, help_text=_(u'Imagem do topo da página, com proporção de 1920x300px'))

    class Meta:
        ordering = ["number", "name",]
        db_table = "scout_group_district"
        verbose_name = _(u"Distrito")
        verbose_name_plural = _(u"Distritos")

    def __unicode__(self):
        if not self.name:
            return u"%0.2d" % (self.number)
        else:
            return u"%0.2dº - %s" % (self.number, self.name)

    def get_short_name(self):
        """
        Retorna somente numeral e sigla do estado
        """
        return u"%0.2d" % (self.number)

    @models.permalink
    def get_absolute_url(self):
        return ("district", (), {"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Preenche o title com o valor de name
        """
        self.title = self.name
        self.slug = self.number
        super(District, self).save(*args, **kwargs)

class ScoutGroup(Displayable, RichText, AdminThumbMixin):
    """
    Cadastro de Grupos Escoteiros

    Classes herdadas:
    CLASS Displayable
      atributos herdados:
      status (1=rascunho, 2=publicado)
      published_date
      expiry_date
      short_url
      in_sitemap

    CLASS Sluged
      title
      slug

    CLASS RichText
      content
    """
    name = models.CharField(_(u"Nome"), max_length=500)
    number = models.IntegerField(verbose_name=_(u"Numeral"), null=False, blank=False)
    district = models.ForeignKey(verbose_name=_(u"Distrito"), to=District)
    logo = FileField(verbose_name=_(u"Logo do Grupo"), upload_to="grupos_escoteiros", format="Image", max_length=255,
                     null=True, blank=True, help_text=_(u'Envie uma imagem com proporção de 182x182px'))
    uf = models.CharField(verbose_name=_(u"UF"), max_length=2, choices=UF, null=False, blank=False, default=UF[0][0], help_text=_(u"Estado do Grupo Escoteiro."))
    city = models.CharField(verbose_name=_(u"cidade"), blank=True, max_length=500)
    address = models.CharField(verbose_name=_(u"Endereço"), blank=True, max_length=500)
    cep = models.CharField(verbose_name=_(u"CEP"), blank=True, max_length=8)
    email = models.EmailField(blank=True, max_length=255)
    president_name = models.CharField(verbose_name=_(u"Presidente"), max_length=255)
    image = FileField(verbose_name=_(u"Imagem Destaque"), upload_to="grupos_escoteiros", format="Image", max_length=255,
                     null=True, blank=True, help_text=_(u'Imagem do topo da página, proporção de 1920x300px'))

    objects = SearchableManager()
    search_fields = {"name": 5, "content": 1}

    class Meta:
        ordering = ["number", "name",]
        db_table = "scout_group"
        verbose_name = _(u"Grupo Escoteiro")
        verbose_name_plural = _(u"Grupos Escoteiros")

    def __unicode__(self):
        if not self.name:
            return u"%0.3d - %s" % (self.number, self.uf)
        else:
            return u"%s - %0.3d - %s" % (self.name, self.number, self.uf)

    def get_short_name(self):
        """
        Retorna somente numeral e sigla do estado
        """
        return u"%0.3d - %s" % (self.number, self.uf)

    @models.permalink
    def get_absolute_url(self):
        return ("scout_group", (), {"slug": self.slug})

    def save(self, *args, **kwargs):
        """
        Preenche o title com o valor de name
        """
        self.title = unicode(self)
        self.slug = self.number
        super(ScoutGroup, self).save(*args, **kwargs)