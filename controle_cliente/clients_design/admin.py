from django.contrib import admin
from .models import Cliente, Profissional, SecaoMarcada
# Register your models here.


admin.site.register([Cliente,
                    Profissional,
                     SecaoMarcada])