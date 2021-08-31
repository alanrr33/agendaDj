from django.shortcuts import render
from django.views.generic import (
    ListView,
    TemplateView
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .models import Person,Reunion

from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
    ReunionSerializerLink,
    PersonaPagination,
    CountReunionSerializer,
)

class ListaPersona(ListView):
    template_name="persona/personas.html"
    context_object_name='personas'

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):

    serializer_class=PersonSerializer
    pagination_class=PersonaPagination

    def get_queryset(self):
        return Person.objects.all().order_by('full_name')

class PersonListView(TemplateView):
    template_name='persona/lista.html'

class PersonSearchApiView(ListAPIView):
    serializer_class=PersonSerializer

    def get_queryset(self):
        #filtrar datos

        kword=self.kwargs['kword']



        return Person.objects.filter(
            full_name__icontains=kword
        )
    

class PersonCreateView(CreateAPIView):
    serializer_class=PersonSerializer

class PersonDetailView(RetrieveAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.filter()

class PersonDeleteView(DestroyAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()

class PersonUpdateView(UpdateAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.filter()

class PersonRetrieveUpdateView(RetrieveUpdateAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.filter()

class PersonApiLista(ListAPIView):
    #vista para interactuar con serializador
    #serializer_class=PersonaSerializer
    serializer_class=PersonaSerializer3
    
    def get_queryset(self):
        return Person.objects.all()

"""class ReunionApiLista(ListAPIView):

    serializer_class=ReunionSerializer2
    
    def get_queryset(self):
        return Reunion.objects.all()
"""
class ReunionApiListaLink(ListAPIView):

    serializer_class=ReunionSerializerLink
    
    def get_queryset(self):
        return Reunion.objects.all()

class ReunionByPersonJob(ListAPIView):
    serializer_class=CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()




