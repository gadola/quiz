from django.shortcuts import render
from core.models import Quizziz, Lesson
from .serializers import QuizzizSerializer
from rest_framework import viewsets

# Create your views here.


class QuizzizModelViewSet(viewsets.ModelViewSet):
    queryset = Quizziz.objects.all()
    serializer_class = QuizzizSerializer


