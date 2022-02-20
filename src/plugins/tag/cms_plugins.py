from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import Tag


@plugin_pool.register_plugin
class TagPlugin(CMSPluginBase):
    model = Tag
    name = _("Tag HTML")
    module = _("Generic")
    render_template = "plugins/tag.html"
    text_enabled = True
    allow_children = True
    fieldsets = [
        (None, {"fields": ("tag", "content")}),
        (_("Advanced settings"), {"classes": ("collapse",), "fields": ("attributes",)}),
    ]
