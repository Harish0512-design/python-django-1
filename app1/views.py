from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from .models import Person
from .serializer import PersonSerializer


# Create your views here.
class PersonCreateView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
