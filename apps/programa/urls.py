from django.urls import path
from .views import programa_lista, programa_detalle, programa_create, programa_edit, programa_delete,crear_asignacionBeneficio,detalle_asignacionBeneficio,listado_beneficios,crear_tipoAsistencia,lista_tipoAsistencias


app_name = 'programa'
urlpatterns = [
    # programa views
    path('', programa_lista, name='programa_lista'),
    path('<int:pk>/', programa_detalle, name='programa_detalle'),
    path('create/', programa_create, name='programa_create'),
    path('edit/<int:pk>', programa_edit, name='programa_edit'),
    path('delete/', programa_delete, name='programa_delete'),
    path('crear_beneficio/', crear_asignacionBeneficio, name='crear_beneficio'),
    path('detalle_beneficio/<fecha>/', detalle_asignacionBeneficio, name='detalle_beneficio'),
    path('listar_beneficios/', listado_beneficios, name='listar_beneficios'),
    path('crear_tipoAsistencia/', crear_tipoAsistencia, name='crear_tipoAsistencia'),
    path('listar_tipoAsistencia/', lista_tipoAsistencias, name='listar_tipoAsistencia'),
]
