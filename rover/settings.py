# -*- coding:utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from django.utils.translation import ugettext_lazy as _


######################
# MEZZANINE SETTINGS #
######################

# The following settings are already defined with default values in
# the ``defaults.py`` module within each of Mezzanine's apps, but are
# common enough to be put here, commented out, for conveniently
# overriding. Please consult the settings documentation for a full list
# of settings Mezzanine implements:
# http://mezzanine.jupo.org/docs/configuration.html#default-settings

# Controls the ordering and grouping of the admin menu.
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", ("Notícias", "blog.BlogPost"), "blog.BlogCategory",
       "generic.ThreadedComment", ("Biblioteca de Mídia", "fb_browse"),)),
    ("Equipes", ("mezzanine_people.Person", "mezzanine_people.PersonCategory")),
    ("Grupos | Distritos", ("scout_group.District", "scout_group.ScoutGroup")), #"scout_group.ScoutGroup"
    #("Eventos", ("events.Event", "events.EventBlock", "events.EventProgramation")),
    ("Eventos", ("events.Event", "events.Block", "events.Programation")),
    ("Users", ("auth.User", "auth.Group",)),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),

)

# A three item sequence, each containing a sequence of template tags
# used to render the admin dashboard.
DASHBOARD_TAGS = (
    ("blog_tags.quick_blog", "mezzanine_tags.app_list"),
    ("comment_tags.recent_comments",),
    ("mezzanine_tags.recent_actions",),
)

# A sequence of templates used by the ``page_menu`` template tag. Each
# item in the sequence is a three item sequence, containing a unique ID
# for the template, a label for the template, and the template path.
# These templates are then available for selection when editing which
# menus a page should appear in. Note that if a menu template is used
# that doesn't appear in this setting, all pages will appear in it.

PAGE_MENU_TEMPLATES = (
    (1, _("Top navigation bar"), "pages/menus/dropdown.html"),
    (2, _("Left-hand tree"), "pages/menus/tree.html"),
    (3, _("Footer"), "pages/menus/footer.html"),
)

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
EXTRA_MODEL_FIELDS = (
    # (
    #     # Dotted path to field.
    #     "mezzanine.blog.models.BlogPost.image",
    #     # Dotted path to field class.
    #     "somelib.fields.ImageField",
    #     # Positional args for field class.
    #     (_("Image"),),
    #     # Keyword args for field class.
    #     {"blank": True, "upload_to": "blog"},
    # ),
    # Example of adding a field to *all* of Mezzanine's content types:

    # Add Field Page
    (
        "mezzanine.pages.models.Page.image",
        "mezzanine.core.fields.FileBrowseField", # 'django.db.models.' is implied if path is omitted.
        (_(u"Imagem Destaque"),),
        {'format': "Image", 'max_length': 255, 'blank': True, 'help_text': u"Proporção 1920x300px."},
    ),
    (
        # Add Fields BlogPost
        "mezzanine.blog.models.BlogPost.image_top",
        "mezzanine.core.fields.FileBrowseField",
        (_(u"Imagem destaque topo"),),
        {
            'directory': "blog",
            'format': "Image", 'max_length': 255, 'null': True, 'blank': True,
            'help_text': _(u"Imagem do topo da notícia, resolução mínima 1920x300px ou proporcional.")
        },

    ),
)

MIGRATION_MODULES = {
    "pages": "rover_core.migrations.pages_migration",
    "blog": "rover_core.migrations.blog_migration",
    #"forms": "path.to.migration.storage.forms_migration",
    #"galleries": "path.to.migration.storage.galleries_migration",
}

# If True, the django-modeltranslation will be added to the
# INSTALLED_APPS setting.
USE_MODELTRANSLATION = False

# BLOG SETTINGS
BLOG_USE_FEATURED_IMAGE = True
BLOG_SLUG = 'noticias'
BLOG_POST_PER_PAGE = 6

SEARCH_MODEL_CHOICES = ('pages.Page', 'blog.BlogPost', 'scout_group.District', 'scout_group.ScoutGroup',
    'mezzanine_file_collections.MediaFile',)

# Metodo padrao utilizado na geracao das URLs slugs
SLUGIFY = 'django.template.defaultfilters.slugify'

########################
# MAIN DJANGO SETTINGS #
########################

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['127.0.0.1',]

ADMINS = (
    ('Rober Guerra', 'roberzguerra@gmail.com'),
)
MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "America/Sao_Paulo"

# If you set this to True, Django will use timezone-aware datetimes.
USE_TZ = False
DATETIME_FORMAT = 'd/m/y H:i:s'
DATE_INPUT_FORMATS = ('%d/%m/%Y',)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "pt-br"

# Supported languages
LANGUAGES = (
    ('en', _('English')),
    ('pt-br', _(u'Português')),
)

# A boolean that turns on/off debug mode. When set to ``True``, stack traces
# are displayed for error pages. Should always be set to ``False`` in
# production. Best set to ``True`` in local_settings.py
DEBUG = False
SERVER_STATIC_FILES = False

# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)

# The numeric mode to set newly-uploaded files to. The value should be
# a mode you'd pass directly to os.chmod.
FILE_UPLOAD_PERMISSIONS = 0o644
FILEBROWSER_MAX_UPLOAD_SIZE = 429916160
FILEBROWSER_EXTENSIONS = {
    'Folder': [''],
    'Image': ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.svg'],
    'Video': ['.mov', '.wmv', '.mpeg', '.mpg', '.avi', '.rm'],
    'Document': ['.pdf', '.doc', '.rtf', '.txt', '.xls', '.xlsx', '.csv', '.docx'],
    'Audio': ['.mp3', '.mp4', '.wav', '.aiff', '.midi', '.m4p'],
    'Code': ['.html', '.py', '.js', '.css']
}

# Tuple of IP addresses, as strings, that:
#   * See debug comments, when DEBUG is true
#   * Receive x-headers
INTERNAL_IPS = ("127.0.0.1",)


#############
# DATABASES #
#############

DATABASES = {
    "default": {
        # Add "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.",
        # DB name or path to database file if using sqlite3.
        "NAME": "",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}


#########
# PATHS #
#########

# Full filesystem path to the project.
PROJECT_APP_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_APP = os.path.basename(PROJECT_APP_PATH)
PROJECT_ROOT = BASE_DIR = os.path.dirname(PROJECT_APP_PATH)

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_APP

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = STATIC_URL + "media/"

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))

# Package/module name to import the root urlpatterns from for the project.
ROOT_URLCONF = "%s.urls" % PROJECT_APP

# Put strings here, like "/home/html/django_templates"
# or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     "django.template.loaders.filesystem.Loader",
#     "django.template.loaders.app_directories.Loader",
# )


################
# APPLICATIONS #
################

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    "mezzanine.pages",
    "mezzanine.blog",
    "mezzanine.forms",
    "mezzanine.galleries",
    "mezzanine.twitter",
    # "mezzanine.accounts",
    # "mezzanine.mobile",

    # Adicionados
    "rover_core",
    "bootstrap3",
    "mezzanine_people",
    "mezzanine_file_collections",
    "ajax_select",

    # Criados
    "institutional",
    "events",
    "scout_group",
)

TEMPLATE_ACCESSIBLE_SETTINGS = ('ACCOUNTS_APPROVAL_REQUIRED', 'ACCOUNTS_VERIFICATION_REQUIRED', 'ADMIN_MENU_COLLAPSED',
    'BITLY_ACCESS_TOKEN', 'BLOG_USE_FEATURED_IMAGE', 'COMMENTS_DISQUS_SHORTNAME', 'COMMENTS_NUM_LATEST',
    'COMMENTS_DISQUS_API_PUBLIC_KEY', 'COMMENTS_DISQUS_API_SECRET_KEY', 'COMMENTS_USE_RATINGS', 'DEV_SERVER',
    'FORMS_USE_HTML5', 'GRAPPELLI_INSTALLED', 'GOOGLE_ANALYTICS_ID', 'JQUERY_FILENAME', 'JQUERY_UI_FILENAME',
    'LOGIN_URL', 'LOGOUT_URL', 'SITE_TITLE', 'SITE_TAGLINE', 'USE_L10N', 'USE_MODELTRANSLATION',)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "mezzanine.conf.context_processors.settings",
    "mezzanine.pages.context_processors.page",
)

# List of middleware classes to use. Order is important; in the request phase,
# these middleware classes will be applied in the order given, and in the
# response phase the middleware will be applied in reverse order.
MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment if using internationalisation or localisation
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.RedirectFallbackMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    "mezzanine.core.middleware.SitePermissionMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

# Store these package names here as they may change in the future since
# at the moment we are using custom forks of them.
PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"

#########################
# OPTIONAL APPLICATIONS #
#########################

# These will be added to ``INSTALLED_APPS``, only if available.
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

# GRAPPELLI SETTINGS ###
GRAPPELLI_ADMIN_TITLE = u"Escoteiros RS"
# END GRAPPELLI SETTINGS ##############

# RICHTEXT SETTINGS ###
RICHTEXT_FILTER_LEVEL = 3
RICHTEXT_ALLOWED_TAGS = ('a', 'abbr', 'acronym', 'address', 'area', 'article', 'aside', 'b', 'bdo', 'big', 'blockquote',
    'br', 'button', 'caption', 'center', 'cite', 'code', 'col', 'colgroup', 'dd', 'del', 'dfn', 'dir', 'div', 'dl',
    'dt', 'em', 'fieldset', 'figure', 'font', 'footer', 'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'header', 'hr', 'i',
    'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'map', 'men', 'nav', 'ol', 'optgroup', 'option', 'p', 'pre',
    'q', 's', 'samp', 'section', 'select', 'small', 'span', 'strike', 'strong', 'sub', 'sup', 'table', 'tbody', 'td',
    'textarea', 'tfoot', 'th', 'thead', 'tr', 'tt', '', 'ul', 'var', 'wbr', 'style', 'script',)
RICHTEXT_ALLOWED_STYLES = ('margin-top', 'margin-bottom', 'margin-left', 'margin-right', 'float', 'vertical-align', 'border', 'margin','color','text-decoration',)



# <style>
# .link-seja-escoteiro {
# color: #00accd;
# }
# </style>

TINYMCE_SETUP_JS = 'rover_core/js/tinymce_setup.js'
# END RICHTEXT SETTINGS ##############

# FILEBROWSER SETTINGS ###
FILEBROWSER_NORMALIZE_FILENAME = True
FILEBROWSER_ADMIN_THUMBNAIL = 'admin_thumbnail'
FILEBROWSER_VERSIONS = {
    #'admin_thumbnail': {'verbose_name': 'Admin Thumbnail', 'width': 60, 'height': 60, 'opts': 'crop'},
    #'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    #'small': {'verbose_name': 'Small (2 col)', 'width': 140, 'height': '', 'opts': ''},
    #'medium': {'verbose_name': 'Medium (4col )', 'width': 300, 'height': '', 'opts': ''},
    #'big': {'verbose_name': 'Big (6 col)', 'width': 460, 'height': '', 'opts': ''},
    #'large': {'verbose_name': 'Large (8 col)', 'width': 680, 'height': '', 'opts': ''},
    'thumbnail': {'verbose_name': 'Thumbnail (1 col)', 'width': 60, 'height': 60, 'opts': 'crop'},
    'medium': {'verbose_name': 'Medium (4col )', 'width': 460, 'height': 260, 'opts': 'crop'},
}
# END FILEBROWSER SETTINGS ###

# MEZANINE PEOPLE SETTINGS ########
PEOPLE_PER_PAGE = 10
#END MEZANINE PEOPLE SETTINGS ####################


##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.

# Instead of doing "from .local_settings import *", we use exec so that
# local_settings has full access to everything defined in this module.

f = os.path.join(PROJECT_APP_PATH, "local_settings.py")
if os.path.exists(f):
    exec(open(f, "rb").read())


# Configuracoes de email
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  #Envia email real
# EMAIL_HOST = 'smtp.gmail.com'  #default='localhost'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #Envia um email no console (terminal)
#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend' #nao envia email (não faz nada)

####################
# DYNAMIC SETTINGS #
####################

# set_dynamic_settings() will rewrite globals based on what has been
# defined so far, in order to provide some better defaults where
# applicable. We also allow this settings module to be imported
# without Mezzanine installed, as the case may be when using the
# fabfile, where setting the dynamic settings below isn't strictly
# required.
try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
