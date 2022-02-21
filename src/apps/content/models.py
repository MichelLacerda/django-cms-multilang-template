from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from djangocms_text_ckeditor.fields import HTMLField
from parler.models import TranslatableModel, TranslatedFields

from django.contrib.auth.models import User

class Content(TranslatableModel):

    translations = TranslatedFields(
        title=models.CharField(
            _("Title"),
            max_length=255,
        ),
        body=HTMLField(
            blank=True,
            null=True,
        ),
        author=models.ForeignKey(
            User,
            on_delete=models.SET_NULL,
            null=True,
        ),
    )

    class Meta:
        verbose_name = _("content")
        verbose_name_plural = _("contents")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("content_detail", kwargs={"pk": self.pk})
