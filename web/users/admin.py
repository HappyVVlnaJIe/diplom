from django.contrib import admin
from .dynamic_models import dva, odin, common


admin.site.register(dva)
admin.site.register(odin)
admin.site.register(common)
