# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import permission_required


def events_permission_required(perm, login_url='/admin/login', raise_exception=False):
    """
    Sobrescreve o metodo que exige login para acessar a view
    Usar com decorator sobre o metodo que desejar o login:
    @method_decorator(events_login_required)
    """
    return permission_required(perm, login_url=login_url, raise_exception=raise_exception)