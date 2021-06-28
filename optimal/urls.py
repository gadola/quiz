from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ,name='home'),
    path('vi/', views.vietnamese ,name='vi'),
    path('en/', views.english ,name='en'),
    # path('<int:pk>/', views.detail ,name='detail'),

    path('ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),
    path('vi/ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),
    # path('', views.getjson ,name='json'),
    path('en/ajax/<int:pk>/', views.get_ajax_quizziz ,name='ajax'),
    path('quiz/', views.QuizzizFormView.as_view() ,name='quiz'),
    path('lesson/', views.LessonFormView.as_view() ,name='lesson'),
    path('themtu/', views.themTu ,name='themtu'),
    path('formthemtu/', views.formThemTu ,name='formthemtu'),
    path('xoa/', views.xoafile ,name='xoafile'),
    path('tao/', views.taofile ,name='taofile'),
    path('statusfalse/', views.statusfalse ,name='statusfalse'),
    path('word/', views.viewWord ,name='viewword'),
    # path('word/<int:pk>/', views.detailViewWord ,name='detail_word'),
    path('word/<lesson_name>/', views.detailViewWord ,name='detail_word'),
    path('ipa/', views.taoipa ,name='ipa'),
    path('voca/', views.getVoca ,name='get_voca'),
    path('voca/full/', views.getVocaAPI ,name='get_voca_API'),

]