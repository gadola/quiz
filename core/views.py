from django.shortcuts import render
from core.models import Quizziz,Lesson
from random import randint, random
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
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages 

# đọc điền nghĩa
def index(request):
    lessons = Lesson.objects.all()
    rd_words = Quizziz.objects.all().order_by('?')[:12]

    paginator = Paginator(lessons, 16)
    page = request.GET.get('page', 1)
    try:
        lessons_paged = paginator.page(page)
    except PageNotAnInteger:
        lessons_paged = paginator.page(1)
    except EmptyPage:
        lessons_paged = paginator.page(paginator.num_pages)
    context = {
        'rd_words':rd_words,
        'lessons':lessons_paged,
    }
    return render(request, 'core/home.html', context)

#nghe điền nghĩa
def NgheDienNghia(request):
    lessons = Lesson.objects.all()
    rd_words = Quizziz.objects.all().order_by('?')[:13]
    paginator = Paginator(lessons, 16)
    page = request.GET.get('page', 1)
    try:
        lessons_paged = paginator.page(page)
    except PageNotAnInteger:
        lessons_paged = paginator.page(1)
    except EmptyPage:
        lessons_paged = paginator.page(paginator.num_pages)
    context = {
        'rd_words':rd_words,
        'lessons':lessons_paged,
    }
    return render(request, 'core/NgheDienNghia.html', context)

#nghe điền từ
def NgheDienTu(request):
    lessons = Lesson.objects.all()
    rd_words = Quizziz.objects.all().order_by('?')[:13]
    paginator = Paginator(lessons, 16)
    page = request.GET.get('page', 1)
    try:
        lessons_paged = paginator.page(page)
    except PageNotAnInteger:
        lessons_paged = paginator.page(1)
    except EmptyPage:
        lessons_paged = paginator.page(paginator.num_pages)
    context = {
        'lessons':lessons_paged,
        'rd_words':rd_words,
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
                title = "Đọc điền nghĩa"
                template = 'core/XuLyDocDienTu.html'
            elif kind == "nghedientu":
                title = "Nghe điền từ"
                template = 'core/XuLyNgheDienTu.html'
            elif kind == "nghediennghia":
                title = "Nghe điền nghĩa"
                template = 'core/XuLyNgheDienNghia.html'
            elif kind == "timtutheobai":
                title = "Xem từ"
                template = 'core/GetWordByLesson.html'
            else:
                return HttpResponse("lỗi sever! 1")
            rd_words = Quizziz.objects.all().order_by('?')[:13]
            context = {
                'title':title,
                'lesson':lesson,
                'words':words,
                'rd_words':rd_words,

            }
        return render(request, template, context)
    else:
        return HttpResponse("lỗi sever!")


class LessonFormView(View):
    def get(self,request):
        form = LessonForm()
        rd_words = Quizziz.objects.all().order_by('?')[:12]

        context = {
           "form":form, 
           "rd_words":rd_words, 
        }
        return render(request, 'core/ThemBaiHoc.html', context)

    def post(self,request):
        form = LessonForm()
        if request.method == 'POST':
            form = LessonForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Create successful!" )
                return redirect('/')
        return HttpResponse("Method is not POST")


class QuizzizFormView(View):
    def get(self,request):
        rd_words = Quizziz.objects.all().order_by('?')[:12]
        lessons = Lesson.objects.all()
        return render(request,'core/ThemTu.html',{'lessons':lessons, 'rd_words':rd_words,})

    def post(self,request):
        if request.method == 'POST':
            lesson = Lesson.objects.get(lesson_name = request.POST.get('lesson',None))
            for i in range(0,int(request.POST.get("number",None))):
                word = request.POST.get('word'+str(i),"")
                mean = request.POST.get('mean'+str(i),"")
                note = request.POST.get('note'+str(i),"")
                ipa = SetIPA(word)
                word = ClearInput(word)
                mean = ClearInput(mean)
                note = ClearInput(note)
                if word != "":
                    if request.POST.get('vital'+str(i),"off")=="on":
                        vital = True
                    else:
                        vital = False
                    if CheckExistWord(word):
                        Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=True,ipa=ipa).save()
                    else:
                        Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=False,ipa=ipa).save()
            GetMP3()
            messages.success(request, "Create successful!" )
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


def XemTu(request):
    lessons = Lesson.objects.all()
    rd_words = Quizziz.objects.all().order_by('?')[:13]
    paginator = Paginator(lessons, 16)
    page = request.GET.get('page', 1)
    try:
        lessons_paged = paginator.page(page)
    except PageNotAnInteger:
        lessons_paged = paginator.page(1)
    except EmptyPage:
        lessons_paged = paginator.page(paginator.num_pages)
    context = {
        'lessons':lessons_paged,
        'rd_words':rd_words,

    }
    return render(request, 'core/XemTu.html',context)


def FindAllWord(request):
    lessons = Lesson.objects.all()
    words = Quizziz.objects.all()
    rd_words = Quizziz.objects.all().order_by('?')[:13]
    context = {
        'words':words,
        'lessons':lessons,
        'rd_words':rd_words,
    }
    return render(request, 'core/TimTu.html',context)


def RandomWord(request):
    rd_words = Quizziz.objects.all().order_by('?')[:13]
    context = {
        'rd_words':rd_words,
    }
    return render(request, 'core/Random.html', context)



def XuLyRandomWord(request):
    ws = Quizziz.objects.all()
    words = []
    number = int(request.POST.get('so',0))
    for i in range(0,number):
        r  = random.randrange(0, ws.count())
        try:
            print(ws[r])
            words.append(ws[r])

        except:
            pass
    rd_words = Quizziz.objects.all().order_by('?')[:13]

    context = {
        'rd_words':rd_words,
        'words':words,
    }
    return render(request, 'core/XuLyRandom.html', context)


def TaoBaiHocTheoMau(request):

    for i in range(1,20):
        Lesson.objects.create(lesson_name = 'Page ' + str(i) + ' Sheets 1')
    for i in range(1,29):
        Lesson.objects.create(lesson_name = 'Page ' + str(i) + ' Sheets 2')

    return redirect('/')

class QuizUpdate(View):
    def get(self,request,pk):
        rd_words = Quizziz.objects.all().order_by('?')[:12]
        lesson = Lesson.objects.get(pk = pk)
        words = Quizziz.objects.filter( lesson = lesson)
        context = {
            'lessons':lesson, 
            'rd_words':rd_words,
            'words':words,
        }
        return render(request,'core/HandleUpdateWords.html',context)

    def post(self,request,pk):
        lesson = Lesson.objects.get(pk = pk)
        if request.method == 'POST':
            for i in range(0,int(request.POST.get("number",None))):
                print(request.POST.get("number",None))
                id = request.POST.get('id'+str(i),-1)
                word = request.POST.get('word'+str(i),"")
                mean = request.POST.get('mean'+str(i),"")
                note = request.POST.get('note'+str(i),"")
                ipa = SetIPA(word)
                word = ClearInput(word)
                mean = ClearInput(mean)
                note = ClearInput(note)
                if id != -1:
                    try:
                        quiz = Quizziz.objects.get(pk = id)
                        if word != "" :
                            if request.POST.get('vital'+str(i),"off")=="on":
                                vital = True
                            else:
                                vital = False
                            quiz.word = word
                            quiz.ipa = ipa
                            quiz.answer = mean
                            quiz.note = note
                            quiz.highlight = vital
                            quiz.save()
                    except:
                        print("quiz id not valid ",id)
                else:
                    if word != "":
                        if request.POST.get('vital'+str(i),"off")=="on":
                            vital = True
                        else:
                            vital = False
                        if CheckExistWord(word):
                            Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=True,ipa=ipa).save()
                        else:
                            Quizziz(word=word,answer=mean,lesson=lesson,note=note,highlight=vital,status=False,ipa=ipa).save()
            GetMP3()
            messages.success(request, "Update successful!" )
            return redirect(request.META.get('HTTP_REFERER'))
        return HttpResponse("method is not POST")
    
def UpdateWords(request):
    lessons = Lesson.objects.all()
    rd_words = Quizziz.objects.all().order_by('?')[:12]

    paginator = Paginator(lessons, 16)
    page = request.GET.get('page', 1)
    try:
        lessons_paged = paginator.page(page)
    except PageNotAnInteger:
        lessons_paged = paginator.page(1)
    except EmptyPage:
        lessons_paged = paginator.page(paginator.num_pages)
    context = {
        'rd_words':rd_words,
        'lessons':lessons_paged,
    }
    return render(request, 'core/UpdateWords.html', context)