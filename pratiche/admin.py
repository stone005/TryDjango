from django.contrib import admin

from .models import Pratica, Agente, Tipo, Fncr

# Register your models here.
admin.site.register(Pratica)
admin.site.register(Agente)
admin.site.register(Tipo)
admin.site.register(Fncr)
