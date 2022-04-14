from .models import Note, Category, Event
from rest_framework.serializers import *

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id',
            'note_title',
            'note_text',
            'created_on',
            # 'updated_on',
            # 'due_by',
            'note_category'
        ]

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'