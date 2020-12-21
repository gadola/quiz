from django.db import models

# Create your models here.


class Lesson(models.Model):
    objects = models.Manager()
    lesson_name = models.CharField(default='', max_length=255)

    def __str__(self):
        return self.lesson_name


class Quizziz(models.Model):
    objects = models.Manager()
    word = models.CharField(default='',max_length=255)
    answer = models.CharField(default='', max_length=500)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.word