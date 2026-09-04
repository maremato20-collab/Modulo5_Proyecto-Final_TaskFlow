from django.contrib import admin
from .models import Proyecto, Tarea


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'usuario', 'created_at')
    search_fields = ('nombre', 'usuario__username')


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'estado', 'proyecto', 'created_at')
    list_filter = ('estado',)
    search_fields = ('titulo', 'proyecto__nombre')