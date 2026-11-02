from django.contrib import admin

from .model.location import Koordinata, Tuman, Viloyat
from .model.media import Image, Video
from .model.qulaylik import MulkQulaylik, Qulaylik
from .models import Mulk

admin.site.register(Qulaylik)
admin.site.register(MulkQulaylik)


class TumanInline(admin.TabularInline):
    model = Tuman
    extra = 1


@admin.register(Viloyat)
class ViloyatAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]  # noqa: RUF012
    inlines = [TumanInline]  # noqa: RUF012


class KoordinataInline(admin.StackedInline):
    model = Koordinata
    extra = 1
    max_num = 1


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class VideoInline(admin.TabularInline):
    model = Video
    extra = 1


@admin.register(Mulk)
class MulkAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]  # noqa: RUF012
    list_filter = ["mulk_turi", "mulk_status", "elon_status"]  # noqa: RUF012
    inlines = [KoordinataInline, ImageInline, VideoInline]  # noqa: RUF012
