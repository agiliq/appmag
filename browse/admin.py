from django.contrib import admin
from browse.models import *


class MorelinksInline(admin.TabularInline):
    model = morelinks
    extra = 3


class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'developer', 'platform', 'price')
    search_fields = ('title', 'category__slug')
    inlines = [MorelinksInline]

admin.site.register(Developer)
admin.site.register(Thumbnail)
admin.site.register(App, AppAdmin)
admin.site.register(Device)
admin.site.register(Category)
