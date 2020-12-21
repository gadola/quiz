from django.shortcuts import render
from core.models import Quizziz,Lesson
from random import randint
from django.http import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponse
from django.views import View
from .forms import QuizzizForm,LessonForm
from django.shortcuts import redirect
from gtts import gTTS
# Create your views here.
import os

def make_mp3(request,pk):
    quizs = Quizziz.objects.all()
    for quiz in quizs:
        try:
            say = gTTS(quiz.answer,lang='en')
            name = quiz.answer+".mp3"
            say.save(name)
            os.rename(name,'media/mp3/'+name)
            quiz.status = True
        except:
            print("đã tồn tại .mp3")
    context = {
        'quizs':quizs,
    }
    return render(request,'core/mp3.html',context)

def index(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request,'core/index.html',context)


def get_ajax_quizziz(request,pk):
    quizzizs = Quizziz.objects.filter(lesson=pk)
    ser_quizzizs = serializers.serialize('json', quizzizs)
    return HttpResponse(json.dumps({"quizzizs": ser_quizzizs}), content_type="application/json")
    # return JsonResponse({"quizzizs": ser_quizzizs}, status=200)

class QuizzizFormView(View):

    def get(self,request):
        form = QuizzizForm()
        return render(request,'core/play.html',{'form':form})

    def post(self,request):
        form = QuizzizForm()
        if request.method == 'POST':
            form = QuizzizForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'core/play.html',{"form":form})

    
class LessonFormView(View):

    def get(self,request):
        form = LessonForm()
        return render(request,'core/test.html',{'form':form})

    def post(self,request):
        form = LessonForm()
        if request.method == 'POST':
            form = LessonForm(request.POST)
            if form.is_valid():
                
                form.save()
                return redirect('/')
        return render(request,'core/test.html',{"form":form})

