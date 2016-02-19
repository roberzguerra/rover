# -*- coding:utf-8 -*-
from mezzanine.utils.models import upload_to
from mezzanine_people.models import PersonCategory

try:
    from urllib import unquote
except ImportError:  # assume python3
    from urllib.parse import unquote
from string import punctuation

from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.sites.models import Site

from mezzanine.core.fields import FileField
from mezzanine.core.models import Orderable
from mezzanine.pages.models import Page, RichText
from mezzanine.blog.models import BlogPost
from mezzanine.conf import register_setting

from scout_group.models import ScoutGroup, District


class BlogPostExtend:
    """
    Alteracoes no model BlogPost
    """
    #in_sitemap = models.BooleanField(_("Show in sitemap"), default=False)

    # image_middle = FileField(verbose_name=_("Imagem destaque centro"),
    #     upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
    #     format="Image", max_length=255, null=True, blank=True,
    #     help_text=_(u"Imagem do centro da página, resolução mínima de 460x260px."))

    def publish_date_post(self):
        return self.publish_date.strftime("Publicado em %d/%m/%Y às %H:%M")

    def publish_date_post_list(self):
        return self.publish_date.strftime("%d/%m/%Y às %H:%M")

    def get_category_first(self):
        return self.categories.first()


BlogPost.__bases__ += (BlogPostExtend,)


class Team(Page, RichText):
    """
    Pagina de Equipes
    """
    categories = models.ManyToManyField("mezzanine_people.PersonCategory", verbose_name=_(u"Equipes"), blank=True,
        related_name="people_category", help_text=_(u"Selecione as equipes para exibir na página."))

    class Meta:
        db_table = "institutional_team"
        verbose_name = _(u"Equipe")
        verbose_name_plural = _(u"Equipes")


class ScoutGroupPage(Page, RichText):
    """
    Pagina de Grupos Escoteiros
    """

    TYPE_GROUP_ALPHA = 1
    TYPE_GROUP_NUMBER = 2
    TYPE_GROUP_DISTRICT = 3
    TYPE_GROUP_ONLY_DISTRICT = 4

    TYPE_PAGE = (
        (TYPE_GROUP_ALPHA, _(u"Grupos em ordem Alfabética")),
        (TYPE_GROUP_NUMBER, _(u"Grupos por Númeral")),
        (TYPE_GROUP_DISTRICT, _(u"Grupos por Distritos")),
        (TYPE_GROUP_ONLY_DISTRICT, _(u"Somente Distritos")),
    )

    type = models.IntegerField(verbose_name=_(u"Tipo de Exibição"), choices=TYPE_PAGE, max_length=2,
        help_text=_(u"Tipo de exibição dos itens da página"))

    class Meta:
        db_table = "institutional_scout_group_page"
        verbose_name = _(u"Grupo | Distrito")
        verbose_name_plural = _(u"Grupos | Distritos")

    def get_scout_groups_type_alpha(self):
        """
        Retorna uma lista de Grupos escoteiros ordenados pelo nome
        """
        return ScoutGroup.objects.published().order_by('name')

    def get_scout_groups_type_number(self):
        """
        Retorna uma lista de Grupos escoteiros ordenados pelo Numeral
        """
        return ScoutGroup.objects.published().order_by('number')

    def get_scout_groups_type_district(self):
        """
        Retorna uma lista de Distritos
        """
        return District.objects.published().order_by('number')


class Slide(Orderable):
    """
    Slide para diversas paginas
    """
    URL_ACCESS_DEFAULT = 1 # Abre na mesma Janela
    URL_ACCESS_NEW = 2 # Abre em nova Janela
    URL_ACCESS = (
        ('1', _(u"Mesma Janela/Aba")),
        ('2', _(u"Nova Janela/Aba")),
    )

    image = FileField(_(u'Imagem 1920x718px'), max_length=255, upload_to='slides', format='Image', help_text=_(u"Envie imagens com resolução de 1920x718px ou equivalente."))
    description = models.CharField(_(u'Descrição'), blank=True, max_length=500, help_text=_(u"Descrição"))
    url = models.CharField(_(u'URL'), blank=True, max_length=500, help_text=_(u"Cole aqui a URL de destino do link."))
    url_access = models.CharField(u'Tipo de Acesso', choices=URL_ACCESS, max_length=1, blank=False,
        help_text=_(u"Tipo de acesso à URL."))
    page = models.ForeignKey(Page, null=True, help_text=_(u""))

    class Meta:
        verbose_name = _(u'Slide')
        verbose_name_plural = _(u'Slides')
        ordering = ['_order']

    def __unicode__(self):
        return self.description

    def get_url_access_html(self):
        html = ''
        if self.url_access == self.URL_ACCESS_NEW:
            html = 'target="_blank"'
        return html

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = unquote(self.file.url).split('/')[-1].rsplit('.', 1)[0]
            name = name.replace("'", '')
            name = ''.join([c if c not in punctuation else ' ' for c in name])
            # str.title() doesn't deal with unicode very well.
            # http://bugs.python.org/issue6412
            name = ''.join([s.upper() if i == 0 or name[i - 1] == ' ' else s
                            for i, s in enumerate(name)])
            self.description = name
        super(Slide, self).save(*args, **kwargs)


class HomePage(Page, RichText):
    """
    Modelo de Página inicial, para cadastrar paginas iniciais para os ramos, por exemplo.

    """
    #slides = models.ManyToManyField(verbose_name=_(u"Slides em Destaque"), to=Slide)

    blog_posts = models.ManyToManyField(verbose_name=_(u"Notícias em Destaque"), to=BlogPost, null=True, blank=True,
                                        help_text=_(u"Notícias para exibir em destaque na página."),)
    teams = models.ManyToManyField(verbose_name=_(u"Equipes em Destaque"), to=PersonCategory, null=True, blank=True,
                                   help_text=_(u"Equipes em destaque para exibir na página."))

    class Meta:
        verbose_name = _(u'Página Inicial')
        verbose_name_plural = _(u'Páginas Iniciais')


class SocialLinks(Orderable):
    """
    Links para Redes Sociais
    """

    SOCIAL_LiNKS = {
        '1': {
            'name': _(u"Facebook"),
            'css_class': 'facebook ir btn',
        },
        '2': {
            'name': _(u"Youtube"),
            'css_class': 'youtube ir btn',
        },
        '3': {
            'name': _(u"Twitter"),
            'css_class': 'twitter ir btn',
        }
    }

    # ID, Name, ClassCSS
    SOCIAL_LINKS_TYPE = (
        ('1', SOCIAL_LiNKS['1']['name']),
        ('2', SOCIAL_LiNKS['2']['name']),
        ('3', SOCIAL_LiNKS['3']['name']),
    )

    type = models.CharField(_(u"Tipo"), choices=SOCIAL_LINKS_TYPE, max_length=1, blank=False)
    url = models.URLField(_(u'Url'), blank=False, max_length=500, help_text=_(u"Link da Rede Social"))
    page = models.ForeignKey(HomePage)

    class Meta:
        verbose_name = _(u'Link')
        verbose_name_plural = _(u'Links')
        ordering = ['type', 'url']

    def __unicode__(self):
        return self.url

    def get_type(self):
        return self.SOCIAL_LiNKS.get(self.type)

