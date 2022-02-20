from django.db import models
from django.utils.translation import ugettext_lazy as _


class TagChoices(models.TextChoices):

    DIV = "div", _("Div")
    SECTION = "section", _("Section")
    H1 = "h1", _("Header 1")
    H2 = "h2", _("Header 2")
    H3 = "h3", _("Header 3")
    H4 = "h4", _("Header 4")
    H5 = "h5", _("Header 5")
    H6 = "h6", _("Header 5")
    P = 'p', _('Paragraph')
