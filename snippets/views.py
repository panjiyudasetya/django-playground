# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetModelSerializer

# Create your views here.
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer
