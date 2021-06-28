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
from quizziz.settings import BASE_DIR
import eng_to_ipa as ipa


# đọc điền nghĩa
def index(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request, 'core/home.html', context)

#nghe điền nghĩa
def NgheDienNghia(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request, 'core/NgheDienNghia.html', context)

#nghe điền từ
def NgheDienTu(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request, 'core/NgheDienTu.html', context)


def XuLy(request):
    if request.method == "POST":
        form = request.POST
        lesson_id = form.get("lesson_id",None)
        kind =  form.get("kind",None)
        if lesson_id != None:
            lesson = Lesson.objects.get(lesson_name = lesson_id)
            words = Quizziz.objects.filter(lesson = lesson)
            print("================",words)
            if kind == "docdientu":
                template = 'core/XuLyDocDienTu.html'
            elif kind == "nghedientu":
                template = 'core/XuLyNgheDienTu.html'
            elif kind == "nghediennghia":
                template = 'core/XuLyNgheDienNghia.html'
            else:
                return HttpResponse("lỗi sever! 1")
            context = {
                'lesson':lesson,
                'words':words,
            }
        return render(request, template, context)
    else:
        return HttpResponse("lỗi sever!")


class LessonFormView(View):
    def get(self,request):
        form = LessonForm()
        context = {
           "form":form, 
        }
        return render(request, 'core/ThemBaiHoc.html', context)

    def post(self,request):
        form = LessonForm()
        if request.method == 'POST':
            form = LessonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return HttpResponse("Method is not POST")


class QuizzizFormView(View):
    def get(self,request):
        lessons = Lesson.objects.all()
        return render(request,'core/ThemTu.html',{'lessons':lessons})

    def post(self,request):
        if request.method == 'POST':
            lesson = Lesson.objects.get(lesson_name = request.POST.get('lesson',None))
            for i in range(0,int(request.POST.get("number",None))):
                word = request.POST.get('word'+str(i),None)
                mean = request.POST.get('mean'+str(i),None)
                note = request.POST.get('note'+str(i),"")
                ipa = SetIPA(word)
                word = ClearInput(word)
                if word != None:
                    if request.POST.get('vital'+str(i),"off")=="on":
                        vital = True
                    else:
                        vital = False
                    if CheckExistWord(word):
                        Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=True,ipa=ipa).save()
                    else:
                        Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=False,ipa=ipa).save()
            GetMP3()
            return redirect('/')
        return HttpResponse("method is not POST")
        
def SetIPA(word):
    phienam ='/'+ ipa.convert(word)+'/'
    return phienam

def GetMP3():
    quizs = Quizziz.objects.filter(status=False)
    for quiz in quizs:
        numQuizIsLike = Quizziz.objects.filter(word = quiz.word, status = False).count()
        if numQuizIsLike == 1:
            try:
                say = gTTS(quiz.word, lang='en', slow=False)
                name = quiz.word + ".mp3"
                say.save(name)
                os.rename(name,'static/mp3/'+name)
                quiz.status = True
                quiz.save()
                print("create " + name +' sucesses')
            except:
                print("lỗi tạo file " + quiz.word)
        else:
            quiz.status = True
            quiz.save()
    return True


def CheckExistWord(word):
    if Quizziz.objects.filter(word = word).count() >= 1:
        return True
    return False


def ClearInput(input):
    input = input.strip()
    input = input.lower()
    input = input.strip(' \t\n\r')
    return input