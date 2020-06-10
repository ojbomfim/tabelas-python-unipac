from django.contrib import admin
from .models import Empresa
from .models import Funcionario
from .models import Disciplinas
from .models import Professor

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Disciplinas)
admin.site.register(Professor)

