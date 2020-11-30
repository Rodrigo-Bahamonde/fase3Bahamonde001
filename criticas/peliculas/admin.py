from django.contrib import admin

# Register your models here.
from . models import ComentarioDolittle, ComentarioEndgame, ComentarioGuerra, ComentarioJoker

admin.site.register(ComentarioJoker)
admin.site.register(ComentarioEndgame)
admin.site.register(ComentarioGuerra)
admin.site.register(ComentarioDolittle)