from django.contrib import admin
from .models import Cliente, Profissional, SecaoMarcada,Produtos, ItensConsumidos
# Register your models here.


admin.site.register([Cliente,
                    Profissional,
                    SecaoMarcada,
                    Produtos,
                    ItensConsumidos])