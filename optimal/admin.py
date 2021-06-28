from django.contrib import admin
from .models import Quizziz,Lesson
# Register your models here.

class QuizAdmin(admin.ModelAdmin):
    list_display=['word','answer','note','status',"lesson"]
    list_filter = ['word']
    search_fields = ['word']
admin.site.register(Quizziz,QuizAdmin)
admin.site.register(Lesson)
