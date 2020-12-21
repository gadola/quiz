from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add-quiz/', views.QuizzizFormView.as_view() ,name='quiz-form'),
    path('add-lesson/', views.LessonFormView.as_view() ,name='lesson-form'),
    path('ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),

]