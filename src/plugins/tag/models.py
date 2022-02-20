from cms.models import CMSPlugin
from django.db import models
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _
from djangocms_bootstrap5.fields import AttributesField
from djangocms_text_ckeditor.fields import HTMLField
from plugins.tag.constants import TagChoices


class Tag(CMSPlugin):
    tag = models.CharField(
        verbose_name=_("Tag"),
        max_length=32,
        choices=TagChoices.choices,
        default=TagChoices.DIV,
    )

    content = HTMLField(
        configuration="CKEDITOR_SETTINGS_SIMPLE",
        blank=True,
        null=True,
    )

    attributes = AttributesField()

    def get_content_truncated(self):
        if self.content:
            striped = strip_tags(self.content).replace("&shy;", "")
            return Truncator(striped).words(3, truncate="...")
        return ""

    def __str__(self):
        return f"{self.tag.upper()} {self.get_content_truncated()}"
