from django.contrib import admin
from django.apps import apps
# Register your models here.
from . import models

class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)

mdls = apps.get_models()
for model in mdls:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass