from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from .models import Note, Category, Event
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer

# Create your views here.
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # permissions if needed