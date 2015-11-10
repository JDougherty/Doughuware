from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Document

class DocumentList(ListView):
    model = Document

class DocumentCreate(CreateView):
    model = Document
