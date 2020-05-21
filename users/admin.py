from django.contrib import admin
from .dynamic_models import NapravlenieStudenta, SluzhebnajaZapiska, Smeta, OtchetStudenta, osnovnye


admin.site.register(NapravlenieStudenta)
admin.site.register(SluzhebnajaZapiska)
admin.site.register(Smeta)
admin.site.register(OtchetStudenta)
admin.site.register(osnovnye)
