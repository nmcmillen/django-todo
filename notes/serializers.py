from .models import Note, Category, Event
from rest_framework import serializers

class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id',
            'author',
            'title',
            'date',
            'duration',
            'all_day',
        ]