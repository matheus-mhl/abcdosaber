from django.contrib import admin

from turmas.models import Turmas, Ausencia, TurmaAlunos

# Register your models here.
admin.site.register(Turmas)
admin.site.register(Ausencia)
admin.site.register(TurmaAlunos)

