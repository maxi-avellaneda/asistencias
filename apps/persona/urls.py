from django.urls import path
from .views import crear_persona,lista_personas


app_name = 'persona'
urlpatterns = [
    # programa views
    path('crear_persona/', crear_persona, name='crear_persona'),
    path('listar_personas/', lista_personas, name='listar_personas'),
]
