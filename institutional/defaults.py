# -*- coding:utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

register_setting(
    name="HOME_PAGE_SITE",
    label=_(u"Página Inicial do Site"),
    description=_(u"URL da Página, deve ser o que está no campo 'URL' no bloco 'Metadado' do Cadastro de Páginas. Ex: /pagina-inicial"),
    editable=True,
    default=unicode(''),
)
