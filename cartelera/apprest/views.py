from django.shortcuts import render
from .models import Film, Director, Actor
from .serializers import FilmSerializer, DirectorSerializer, ActorSerializer
from rest_framework import viewsets
from datetime import datetime, timedelta, time

today = datetime.now().date()

class FilmViewSet(viewsets.ModelViewSet):
 
    serializer_class = FilmSerializer
    queryset = Film.objects.filter(release__lte=today).order_by('name')

class FilmComingSoonViewSet(viewsets.ModelViewSet):

    serializer_class = FilmSerializer
    queryset = Film.objects.filter(release__gt=today).order_by('release')

class DirectorViewSet(viewsets.ModelViewSet):
 
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()

class ActorViewSet(viewsets.ModelViewSet):
 
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


