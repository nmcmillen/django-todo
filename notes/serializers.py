from .models import Note, Category, Event
from rest_framework.serializers import *

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'
        # [
        #     # potentially add 'url',
        #     'id',
        #     'note_title',
        #     'note_text',
        #     'created_on',
        #     'updated_on',
        #     'due_by',
        #     'note_category'
        # ]