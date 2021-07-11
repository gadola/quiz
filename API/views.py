from django.shortcuts import render
from rest_framework.response import Response
from core.models import Quizziz, Lesson
from .serializers import QuizzizSerializer, LessonSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import filters
# Create your views here.


class QuizzizModelViewSet(viewsets.ModelViewSet):
    queryset = Quizziz.objects.all()
    serializer_class = QuizzizSerializer
    filter_backends = ( filters.OrderingFilter, filters.SearchFilter)
    ordering = ('answer',)
    search_fields = ('word','answer' )

class LessonModelViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = ( filters.OrderingFilter, filters.SearchFilter)
    ordering = ('lesson_name',)
    search_fields = ('lesson_name','id' )


@csrf_exempt
def lessons_list(request):
    if request.method == 'GET':
        lessons = Lesson.objects.all()
        lessons_json = LessonSerializer(lessons, many=True)
        return JsonResponse(lessons_json.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        lessons_json = LessonSerializer(data=data)
        if lessons_json.is_valid():
            lessons_json.save()
            return JsonResponse(lessons_json.data, status=201)
        return JsonResponse(lessons_json.errors, status=400)


@csrf_exempt
def words_detail(request, pk):
    try:
        lesson = Lesson.objects.get(pk=pk)
    except Lesson.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        quizs = Quizziz.objects.all().filter(lesson = lesson)
        quizs_json = QuizzizSerializer(quizs,many=True)
        return JsonResponse(quizs_json.data, safe=False)

