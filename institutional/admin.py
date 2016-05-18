# -*- coding:utf-8 -*-
from copy import deepcopy

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms

from mezzanine.blog.models import BlogPost
from mezzanine.pages.models import Page
from mezzanine.core.admin import DisplayableAdminForm, TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin, PageAdminForm
from mezzanine.blog.admin import BlogPostAdmin, blogpost_fieldsets, blogpost_list_display, blogpost_list_filter
from mezzanine.utils.models import upload_to

from models import Team, ScoutGroupPage, HomePage, Slide, SocialLinks, EventPage
from rover_core.admin import page_fieldsets


class BlogPostAdminForm(DisplayableAdminForm):
    """
    Form customizado para o BlogPost

    Seta o atributo "Exibir no sitemap" como False e não obrigatorio
    """

    in_sitemap = forms.BooleanField(label=_(u"Show in sitemap"), required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super(BlogPostAdminForm, self).__init__(*args, **kwargs)
        self.fields['featured_image'].label = _(u"Imagem destaque")
        self.fields['featured_image'].help_text = _(u"Imagem destaque da notícia, resolução mínima 460x260px ou proporcional.")
        self.fields['image_top'].directory = upload_to("blog.BlogPost.featured_image", "blog")

blogpost_fieldsets[0][1]["fields"].insert(4, "image_top")


class BlogPostAdminRover(BlogPostAdmin):
    """
    Admin class for blog posts.
    """

    fieldsets = blogpost_fieldsets
    list_display = ["title", "publish_date", "user", "status", "admin_link", "created"]
    list_filter = blogpost_list_filter
    filter_horizontal = ("categories", "related_posts",)
    form = BlogPostAdminForm


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, BlogPostAdminRover)


class PageAdminInstitutionalForm(PageAdminForm):
    """
    Form customizado para Paginas do Site

    Seta o atributo "Exibir no sitemap" como False e não obrigatorio
    """
    in_sitemap = forms.BooleanField(label=_(u"Show in sitemap"), required=False, initial=False)


PageAdmin.form = PageAdminInstitutionalForm
admin.site.unregister(Page)
admin.site.register(Page, PageAdmin)

class SocialLinkInline(TabularDynamicInlineAdmin):
    model = SocialLinks


class SlideInline(TabularDynamicInlineAdmin):
    model = Slide


class HomePageAdmin(PageAdmin):
    """
    Admin para a HomePage
     """
    filter_horizontal = ("blog_posts", "teams", )
    inlines = [SlideInline, SocialLinkInline, ]


# admin_classes_with_slides = [HomePageAdmin, ] #FormAdmin, GalleryAdmin]
# for admin_class in admin_classes_with_slides:
#     setattr(admin_class, 'inlines', list(admin_class.inlines) + [SlideInline])


team_fields = deepcopy(page_fieldsets)
team_fields[0][1]["fields"].insert(5, u"categories")

class TeamAdmin(PageAdmin):
    """
    Admin para a Pagina de Equipes
    """

    fieldsets = team_fields

    #fieldsets = ((None, {"fields": ("title",)}),)

    # def in_menu(self):
    #     """
    #     Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
    #     """
    #     for (name, items) in settings.ADMIN_MENU_ORDER:
    #         if "people.PersonCategory" in items:
    #             return True
    #     return False

scout_core_page_fields = deepcopy(page_fieldsets)
scout_core_page_fields[0][1]["fields"].insert(5, u"type")

class ScoutGroupPageAdmin(PageAdmin):
    """
    Admin para a Pagina de Grupos e Distritos
    """
    fieldsets = scout_core_page_fields


event_page_fields = deepcopy(page_fieldsets)

class EventPageAdmin(PageAdmin):
    """
    Admin para a Pagina de Equipes
    """
    fieldsets = event_page_fields


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(ScoutGroupPage, ScoutGroupPageAdmin)
admin.site.register(EventPage, EventPageAdmin)
