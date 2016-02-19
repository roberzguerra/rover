# -*- coding:utf-8 -*-

from django.shortcuts import get_object_or_404
from mezzanine.utils.views import render, paginate
from scout_group.models import ScoutGroup, District


def district(request, slug, template="scout_group/scout_group_page.html"):
    """
    Exibe a página do Distrito
    """
    district = get_object_or_404(District.objects.published(), slug=slug)
    context = {"district": district, "editable_obj": district}
    return render(request, template, context)


def scout_group(request, slug, template="scout_group/scout_group_page.html"):
    """

    """
    scout_group = ScoutGroup.objects.published()
    scout_group = get_object_or_404(scout_group, slug=slug)
    context = {"scout_group": scout_group, "editable_obj": scout_group}
    return render(request, template, context)
