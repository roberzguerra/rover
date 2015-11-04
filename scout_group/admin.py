# -*- coding:utf-8 -*-

from copy import deepcopy
from mezzanine.conf import settings
from mezzanine.core.admin import DisplayableAdmin, DisplayableAdminForm

from django.contrib import admin
from mezzanine.core.models import CONTENT_STATUS_PUBLISHED
from scout_group.models import ScoutGroup, District


# DistrictAdmin
district_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
district_fieldsets[0][1]["fields"][0] = 'name'
district_fieldsets[0][1]["fields"].insert(1, 'number')
district_fieldsets[0][1]["fields"].insert(2, 'logo')
district_fieldsets[0][1]["fields"].extend(["coordinator_name", "email", "uf", "address", "cep", "content", "image" ])

# ScoutGroupAdmin
scout_group_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
scout_group_fieldsets[0][1]["fields"][0] = 'name'
scout_group_fieldsets[0][1]["fields"].insert(1, 'number')
scout_group_fieldsets[0][1]["fields"].insert(2, 'district')
scout_group_fieldsets[0][1]["fields"].insert(3, 'logo')
scout_group_fieldsets[0][1]["fields"].extend(["president_name", "email", "uf", "city", "address", "cep", "content", "image" ]   )



class ScoutGroupForm(DisplayableAdminForm):
    """

    """
    def clean_content(self):
        """
        # Formulario DisplayableAdminForm sobrescrito para remover o conteudo abaixo,
        que obriga que seja informado o content (conteúdo da página)

        status = self.cleaned_data.get("status")
        content = self.cleaned_data.get("content")
        if status == CONTENT_STATUS_PUBLISHED and not content:
            raise ValidationError(_("This field is required if status "
                                    "is set to published."))
        return content
        """
        return self.cleaned_data.get("content")


class DistrictAdmin(DisplayableAdmin):
    """
    Admin para Districts
    """

    fieldsets = district_fieldsets
    list_display = ["admin_thumb", "__unicode__", "status",]
    list_display_links = ['__unicode__', ]
    list_filter = ['name', 'number',]

    form = ScoutGroupForm


class ScoutGroupAdmin(DisplayableAdmin):
    """
    Admin para ScoutGroup
    """
    fieldsets = scout_group_fieldsets
    list_display = ["admin_thumb", "__unicode__", "city", "status",]
    list_display_links = ['__unicode__', ]
    list_filter = ['name', 'number',]

    form = ScoutGroupForm


admin.site.register(District, DistrictAdmin)
admin.site.register(ScoutGroup, ScoutGroupAdmin)