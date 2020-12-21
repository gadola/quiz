from django.core.management.base import BaseCommand
from optimal.models import Quizziz, Lesson
import json



class Command(BaseCommand):
    help = "create default quiz"

    def handle(self, *args, **kwargs):
        json_data = open(r'C:\Users\efert\Project\Python\quizziz\optimal\management\commands\quiz.json', encoding="utf8")
        data1 = json.load(json_data)
        data2 = json.dumps(data1)
        output = json.loads(data2)
        # products = Quizziz.objects.all()
        for product in output:
            # if product['id'] not in [i.id for i in products]:
            Quizziz.objects.create(
                answer = product['answer'],
                word= product['word'],
                lesson= Lesson.objects.get(lesson_name='bai 1')
            )
            print(product['word'])
        