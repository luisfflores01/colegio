from django.contrib import admin
from django.db import transaction
from datetime import datetime as dt
from easy_select2 import select2_modelform
from .models import (
    Asistencia,
    AsistenciaDetalle,
    AsistenciaIndicadoresNegativosGral,
    DetalleIndicadoresNegativos
)

# AsistenciaDetalleForm = select2_modelform(AsistenciaDetalle, attrs={'width': '400px'})


class AsistenciaDetalleInline(admin.TabularInline):
    model = AsistenciaDetalle
    # form = AsistenciaDetalleForm
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    extra = 0

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('estudiante', 'fecha', 'hora_llegada', 'hora_salida', 'fecha_creacion',)
    search_fields = ('estudiante', )
    inlines = [AsistenciaDetalleInline, ]

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(AsistenciaAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset

    @transaction.atomic
    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        asistencia_pk_tmp = 0
        try:
            for obj in formset.deleted_objects:
                obj.fecha_eliminacion = dt.now()
                obj.usuario_eliminacion = request.user
                obj.save()
            for instance in instances:
                if instance.id is not None:
                    instance.fecha_modificacion = dt.now()
                    instance.usuario_modificacion = request.user
                else:
                    asistencia_pk_tmp = instance.asistencia_id
                    instance.asistencia_id = instance.asistencia_id
                    instance.usuario_creacion = request.user
                instance.save()
            formset.save_m2m()
        except Exception as ex:
            print(ex)


@admin.register(DetalleIndicadoresNegativos)
class DetalleIndicadoresNegativosAdmin(admin.ModelAdmin):
    exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
               'fecha_eliminacion',)
    list_display = ('asistenciadetalle', 'indicador_negativo', 'observacion', )
    search_fields = ('indicador_negativo', )

    def save_model(self, request, obj, form, change):
        if change:
            obj.usuario_modificacion = request.user
            obj.fecha_modificacion = dt.now()
        else:
            obj.usuario_creacion = request.user
        super(DetalleIndicadoresNegativosAdmin, self).save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        obj.usuario_eliminacion = request.user
        obj.fecha_eliminacion = dt.now()
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.filter(fecha_eliminacion__isnull=True)
        return queryset


# @admin.register(AsistenciaIndicadoresNegativosGral)
# class AsistenciaIndicadoresNegativosGralAdmin(admin.ModelAdmin):
#     exclude = ('usuario_creacion', 'usuario_modificacion', 'usuario_eliminacion', 'fecha_modificacion',
#                'fecha_eliminacion',)
#     list_display = ('asistencia', 'indicador_negativo', )
#     search_fields = ('indicador_negativo', )
#
#     def save_model(self, request, obj, form, change):
#         if change:
#             obj.usuario_modificacion = request.user
#             obj.fecha_modificacion = dt.now()
#         else:
#             obj.usuario_creacion = request.user
#         super(AsistenciaIndicadoresNegativosGralAdmin, self).save_model(request, obj, form, change)
#
#     def delete_model(self, request, obj):
#         obj.usuario_eliminacion = request.user
#         obj.fecha_eliminacion = dt.now()
#         obj.save()
#
#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         queryset = queryset.filter(fecha_eliminacion__isnull=True)
#         return queryset
