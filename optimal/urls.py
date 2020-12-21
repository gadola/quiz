from django.urls import path, include
from . import views

urlpatterns = [
    path('vi/', views.index ,name='index'),
    path('en/', views.english ,name='en'),
    path('word/', views.word ,name='word'),
    path('word/ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),
    path('vi/ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),
    path('', views.getjson ,name='json'),
    path('en/ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),
    path('quiz/', views.QuizzizFormView.as_view() ,name='quiz'),
    path('lesson/', views.LessonFormView.as_view() ,name='lesson'),

]