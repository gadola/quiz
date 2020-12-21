from django import forms
from .models import Quizziz,Lesson

class QuizzizForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        self.status = kwargs.pop('status',None)
        super().__init__(*args,**kwargs)

    def save(self,commit = True):
        quiz = super().save(commit = False)
        quiz.status = self.status
        quiz.answer = quiz.answer+','
        quiz.save()

    class Meta:
        model = Quizziz
        fields = ['word','answer','lesson']
    


class LessonForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

    def save(self):
        lesson = super().save()
        lesson.save()

    class Meta:
        model = Lesson
        fields = ['lesson_name']