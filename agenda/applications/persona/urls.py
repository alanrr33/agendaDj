from django.urls import path
from .views import (
    ListaPersona,
    PersonListApiView,
    PersonListView,
    PersonSearchApiView,
    PersonCreateView,
    PersonDetailView,
    PersonDeleteView,
    PersonUpdateView,
    PersonRetrieveUpdateView,
    PersonApiLista,
    #ReunionApiLista,
    ReunionApiListaLink,
    ReunionByPersonJob,
    
)

app_name="personas_urls"

urlpatterns = [
    path('personas/',ListaPersona.as_view(),name="listar-personas"),
    path('api/persona/lista/',PersonListApiView.as_view()),
    path('lista/',PersonListView.as_view(),name="lista"),
    path('api/persona/search/<kword>/',PersonSearchApiView.as_view()),
    path('api/persona/create/',PersonCreateView.as_view()),
    path('api/persona/detail/<pk>/',PersonDetailView.as_view(),name='detalle'),
    path('api/persona/delete/<pk>/',PersonDeleteView.as_view()),
    path('api/persona/modificar/<pk>/',PersonRetrieveUpdateView.as_view()),
    path('api/personas/',PersonApiLista.as_view()),
    #path('api/reuniones/',ReunionApiLista.as_view()),
    path('api/reuniones-link/',ReunionApiListaLink.as_view()),
    path('api/reunion/por-job/',ReunionByPersonJob.as_view()),
    

    

]