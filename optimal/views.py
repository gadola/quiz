from django.shortcuts import render
from optimal.models import Quizziz,Lesson
from random import randint
from django.http import JsonResponse
from django.core import serializers
import json
from .forms import QuizzizForm,LessonForm
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect
from gtts import gTTS

# Create your views here.
import os
from quizziz.settings import BASE_DIR
import eng_to_ipa as ipa



# trang chủ
def home(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request,'optimal/home.html',context)

# trang tiếng việt
def vietnamese(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request,'optimal/vietnamese.html',context)


def english(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request,'optimal/english.html',context)





def getVocaAPI(request):
    quizzizs = Quizziz.objects.all()
    ser_quizzizs = serializers.serialize('json', quizzizs)
    return HttpResponse(json.dumps({"quizzizs": ser_quizzizs}), content_type="application/json")

def getVoca(request):
    return render(request, 'optimal/tao.html')

def taoipa(request):
    quizs = Quizziz.objects.all()
    for quiz in quizs:
        phienam ='/'+ ipa.convert(quiz.word)+'/'
        quiz.ipa = phienam
        quiz.save()
    return redirect('/')


def viewWord(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons':lessons,
    }
    return render(request,'optimal/viewword.html',context)

def detailViewWord(request,pk):
    quizs = Quizziz.objects.filter(lesson=pk)
    context = {
        'quizs':quizs,
        'lesson':pk,
    }
    return render(request,'optimal/detailviewword.html',context)

def taofile(request):
    quizs = Quizziz.objects.filter(status=False)
    print(quizs)
    try:
        for quiz in quizs:
            say = gTTS(quiz.word, lang='en', tld='com')
            name = quiz.word+".mp3"
            say.save(name)
            os.rename(name,'static/mp3/'+name)
            quiz.status = True
            quiz.save()
            print("create " +name +' sucesses')
    except:
        pass
    return redirect('/')

def xoafile(request):
    quizs = Quizziz.objects.filter(status=True)
    for quiz in quizs:
        quiz.status = False
        os.remove(BASE_DIR+"\\static\\mp3\\" +quiz.word + '.mp3')
        quiz.save()
    return redirect('/')

def statusfalse(request):
    quizs = Quizziz.objects.all()
    try:
        for quiz in quizs:
            quiz.status = False
            quiz.save()
    except:
        pass
    return HttpResponse("đã false")

# trang chủ




# mode english


# tạo ajax
def getjson(request):
    quizzizs = Quizziz.objects.all()
    ser_quizzizs = serializers.serialize('json', quizzizs)
    return HttpResponse(json.dumps({"quizzizs": ser_quizzizs}), content_type="application/json")

# tạo ajax
def get_ajax_quizziz(request,pk):
    quizzizs = Quizziz.objects.filter(lesson=pk,highlight=True)
    ser_quizzizs = serializers.serialize('json', quizzizs)
    return HttpResponse(json.dumps({"quizzizs": ser_quizzizs}), content_type="application/json")
    # return JsonResponse({"quizzizs": ser_quizzizs}, status=200)


# tạo file audio cho từ vựng
def taoMp3():
    quizs = Quizziz.objects.filter(status=False)
    for quiz in quizs:
        numQuizIsLike = Quizziz.objects.filter(word = quiz.word).count()
        if numQuizIsLike == 1:
            try:
                say = gTTS(quiz.word, lang='en', slow=False)
                name = quiz.word + ".mp3"
                say.save(name)
                os.rename(name,'static/mp3/'+name)
                quiz.status = True
                quiz.save()
                print("create " +name +' sucesses')
            except:
                print("lỗi tạo file " + name)
        else:
            quiz.status = True
            quiz.save()
    return True


def get_word(words):
    try:
        Quizziz.objects.get(word = words)
        return True
    except:
        return False

def themTu(request):
    if request.method == 'POST':
        lesson = Lesson.objects.get(lesson_name = request.POST.get('lesson',None))
        for i in range(0,int(request.POST.get("number",None))):
            word = request.POST.get('word'+str(i),None)
            mean = request.POST.get('mean'+str(i),None)
            note = request.POST.get('note'+str(i),"")
            if request.POST.get('vital'+str(i),"off")=="on":
                vital = True
            else:
                vital = False
            if get_word(word):
                Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=True).save()
            else:
                Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=False).save()
        taoMp3()
        return redirect('/')
    return HttpResponse("method is not POST")
    

def formThemTu(request):
    lessons = Lesson.objects.all()
    return render(request,'optimal/forms.html',{'lessons':lessons})

class QuizzizFormView(View):

    def get(self,request):
        form = QuizzizForm()
        return render(request,'optimal/play.html',{'form':form})

    def post(self,request):
        form = QuizzizForm()
        if request.method == 'POST' :
            if get_word(request.POST['word']):
                form = QuizzizForm(request.POST,status = True)
                print("giong")
            else:
                form = QuizzizForm(request.POST,status = False)
                print("khac")
            if form.is_valid():
                form.save()
                taoMp3()
                return redirect('/quiz/quiz/')
        return render(request,'optimal/play.html',{"form":form})

    
class LessonFormView(View):

    def get(self,request):
        form = LessonForm()
        return render(request,'optimal/test.html',{'form':form})

    def post(self,request):
        form = LessonForm()
        if request.method == 'POST':
            form = LessonForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'optimal/test.html',{"form":form})

