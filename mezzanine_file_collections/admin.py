from django.contrib import admin

from mezzanine.core.admin import TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin
from mezzanine_file_collections.models import MediaLibrary, MediaFile
from rover_core.admin import page_fieldsets as scout_core_page_fields


class MediaFileInline(TabularDynamicInlineAdmin):
    model = MediaFile



class MediaLibraryAdmin(PageAdmin):
    inlines = (MediaFileInline,)
    fieldsets = scout_core_page_fields


admin.site.register(MediaLibrary, MediaLibraryAdmin)
