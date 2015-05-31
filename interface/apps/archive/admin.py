from django.contrib import admin
from archive.models import *


class BaseAdmin(admin.ModelAdmin):
    """
    """
    exclude = ('is_active',)
    pass


@admin.register(Event)
class EventAdmin(BaseAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(BaseAdmin):
    pass


@admin.register(Score)
class ScoreAdmin(BaseAdmin):
    list_display = ('name', 'event', 'project', 'place', 'year')
