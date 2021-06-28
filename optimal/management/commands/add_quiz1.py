from django.core.management.base import BaseCommand
from optimal.models import Quizziz, Lesson
import json



class Command(BaseCommand):
    help = "create default quiz"

    def handle(self, *args, **kwargs):
        json_data = open(r'D:\Projects\quiz\optimal\management\commands\page22.json', encoding="utf8")
        data1 = json.load(json_data)
        data2 = json.dumps(data1)
        output = json.loads(data2)
        n = 0
        # products = Quizziz.objects.all()
        for product in output:
            # if product['id'] not in [i.id for i in products]:
            Quizziz.objects.create(
                word= product["fields"]['word'],
                answer = product["fields"]['answer'],
                note = product["fields"]['note'],
                highlight = product["fields"]['highlight'],
                lesson = Lesson.objects.get(lesson_name='Page 22 Sheets 2')
            )
            print(product["fields"]['word'])
            n=n+1
        print(n)
        