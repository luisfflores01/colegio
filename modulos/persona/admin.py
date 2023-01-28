from django.contrib import admin
from datetime import datetime as dt
from easy_select2 import select2_modelform
from .models import (
    Tutor,
    Estudiante,
    Profesor,
)

TutorForm = select2_modelform(Tutor, attrs={'width': '300px'})
EstudianteForm = select2_modelform(Estudiante, attrs={'width': '300px'})
ProfesorForm = select2_modelform(Profesor, attrs={'width': '300px'})


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    form = TutorForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('documento', 'imagen_tag', 'expedido', 'nombre', 'apellido_paterno', 'apellido_materno',
                    'genero', 'ocupacion', 'tipotutor',)
    search_fields = ('documento', 'nombre', 'apellido_paterno', 'apellido_materno', )
    readonly_fields = ('imagen_preview', )

    def imagen_preview(self, obj):
        return obj.imagen_preview

    def imagen_tag(self, obj):
        return obj.imagen_tag

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(TutorAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    form = EstudianteForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('rude', 'imagen_tag', 'nombre', 'apellido_paterno', 'apellido_materno',
                    'genero', 'tutor', 'documento', 'expedido', 'fecha_nacimiento',)
    search_fields = ('rude', 'documento', 'nombre', 'apellido_paterno', 'apellido_materno', )
    readonly_fields = ('imagen_preview', )

    def imagen_preview(self, obj):
        return obj.imagen_preview

    def imagen_tag(self, obj):
        return obj.imagen_tag

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(EstudianteAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    form = ProfesorForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('documento', 'imagen_tag', 'expedido', 'nombre', 'apellido_paterno', 'apellido_materno',
                    'genero', )
    search_fields = ('documento', 'nombre', 'apellido_paterno', 'apellido_materno', )
    readonly_fields = ('imagen_preview', )

    def imagen_preview(self, obj):
        return obj.imagen_preview

    def imagen_tag(self, obj):
        return obj.imagen_tag

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(ProfesorAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset
