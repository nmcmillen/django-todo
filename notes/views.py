from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from .models import Note, Category, Event
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer, EventSerializer, CategorySerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'author', 'note_title']
    search_fields = ['note_title', 'note_text']
    # permission_classes = [permissions.IsAuthenticated]
    # permissions if needed

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer