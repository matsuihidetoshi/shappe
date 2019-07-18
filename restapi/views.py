from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Question
from .serializer import QuestionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
  queryset = Question.objects.all()
  serializer_class = QuestionSerializer