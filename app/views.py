#encoding:utf-8
from django.views.generic import ListView
from app.models import *

class NoteListView(ListView):
    queryset = Note.objects.all().order_by('-date')
    model = Note
