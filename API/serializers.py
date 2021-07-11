from django.db import models
from core.models import Quizziz, Lesson
from rest_framework import serializers


class QuizzizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizziz
        fields = ('id', 'word', 'ipa', 'answer', 'lesson', 'note', 'highlight')
