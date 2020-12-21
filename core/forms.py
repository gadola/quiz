from django import forms
from .models import Quizziz,Lesson

class QuizzizForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

    def save(self,commit = True):
        quiz = super().save(commit = False)
        quiz.answer = quiz.answer+','
        quiz.save()

    class Meta:
        model = Quizziz
        fields = ['mp3_path','answer','lesson']
    


class LessonForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

    def save(self):
        lesson = super().save()
        lesson.save()

    class Meta:
        model = Lesson
        fields = ['lesson_name']