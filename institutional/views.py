from django.shortcuts import render, get_object_or_404, redirect
from institutional.models import HomePage
from mezzanine.conf import settings

def homepage(request, template="index.html"):
    """
    Direciona para a pagina inicial
    """
    page = get_object_or_404(HomePage, slug=settings.HOME_PAGE_SITE)

    if page:
        return redirect(page.get_absolute_url())
    else:
        return render(request, template)
