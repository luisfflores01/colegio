from datetime import datetime as dt
from django.contrib import admin
from .models import (
    Inscripcion,
)


@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('tipoestudiante', 'estudiante', 'curso', 'gestion', 'fecha_creacion',
                    'usuario_creacion',)
    search_fields = ('tipoestudiante', 'estudiante', 'gestion', )

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(InscripcionAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset

