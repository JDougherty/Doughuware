from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Document


class DocumentList(ListView):
    model = Document


class DocumentCreate(CreateView):
    model = Document
    fields = ('name', 'docfile', 'description', )

    def get_form_class(self):
        form_class = super(DocumentCreate, self).get_form_class()
        form_class.required_css_class = 'field-required'
        form_class.error_css_class = 'error'
        form_class.header = 'Add New Document'
        return form_class
