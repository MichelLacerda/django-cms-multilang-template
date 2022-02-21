from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Content


@admin.register(Content)
class ContentAdmin(TranslatableAdmin):
    ...
