from django.conf.urls import patterns, url

from .views import DocumentList, DocumentCreate

urlpatterns = patterns(
    '',
    url(r'^$', DocumentList.as_view(), name='document_list'),
    url(r'document/create/$', DocumentCreate.as_view(), name='document_create'),
)
