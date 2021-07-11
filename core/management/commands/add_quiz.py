from django.core.management.base import BaseCommand
from core.models import Quizziz, Lesson
import json




class Command(BaseCommand):
    help = "create default quiz"

    def handle(self, *args, **kwargs):
        json_data = open(r'D:\Projects\quizziz\core\management\commands\quiz.json', encoding="utf8")
        data1 = json.load(json_data)
        data2 = json.dumps(data1)
        output = json.loads(data2)
        n = 0
        tenbaihoc = {
                "1":"Page 1 Sheets 1",
                "2":"Page 2 Sheets 1",
                "3":"Page 3 Sheets 1",
                "4":"Page 4 Sheets 1",
                "5":"Page 15 Sheets 1",
                "6":"Page 16 Sheets 1",
                "7":"Page 17 Sheets 1",
                "17":"Page 19 Sheets 1",
                "19":"Page 18 Sheets 1",
                "48":"Page 5 Sheets 1",
                "49":"Page 6 Sheets 1",
                "50":"Page 7 Sheets 1",
                "51":"Page 8 Sheets 1",
                "52":"Page 9 Sheets 1",
                "53":"Page 10 Sheets 1",
                "54":"Page 11 Sheets 1",
                "55":"Page 12 Sheets 1",
                "47":"Page 13 Sheets 1",
                "46":"Page 14 Sheets 1",
                
                "23":"Page 13 Sheets 2",
                "25":"Page 14 Sheets 2",
                "26":"Page 15 Sheets 2",
                "27":"Page 16 Sheets 2",
                "28":"Page 17 Sheets 2",
                "29":"Page 18 Sheets 2",
                "30":"Page 19 Sheets 2",
                "31":"Page 20 Sheets 2",
                "32":"Page 21 Sheets 2",
                "33":"Page 22 Sheets 2",
                "34":"Page 23 Sheets 2",
                "35":"Page 24 Sheets 2",
                "36":"Page 25 Sheets 2",
                "37":"Page 26 Sheets 2",     
                "38":"Page 27 Sheets 2",      
                "44":"Page 28 Sheets 2",
     
            
        }
        # products = Quizziz.objects.all()
        for key in tenbaihoc:
            for product in output:
                if product['fields']['lesson'] == int(key):
                    Quizziz.objects.create(
                        word= product["fields"]['word'],
                        answer = product["fields"]['answer'],
                        note = product["fields"]['note'],
                        ipa = product["fields"]['ipa'],
                        highlight = product["fields"]['highlight'],
                        lesson = Lesson.objects.get(lesson_name=tenbaihoc[key])
                    )
                    print(product["fields"]['word'] )
                    n=n+1
        print(n)
        