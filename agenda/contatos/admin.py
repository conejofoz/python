from django.contrib import admin
from .models import Categoria, Contato


#Essa classe sobreescreve as opções default do django admin
class contatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'categoria')
    list_display_links = ('id', 'nome', 'sobrenome')
    list_filter = ('nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, contatoAdmin)
