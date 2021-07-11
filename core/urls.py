from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/lesson/', views.TaoBaiHocTheoMau, name=''),
    path('vi/', views.NgheDienNghia, name='nghediennghia'),
    path('en/', views.NgheDienTu, name='nghedientu'),
    path('quiz/', views.XuLy, name='xuly'),
    path('them-bai-hoc/', views.LessonFormView.as_view(), name='thembaihoc'),
    path('them-tu/', views.QuizzizFormView.as_view(), name='themtu'),
    path('update-words/', views.UpdateWords, name='updatetu'),
    path('update-words/<int:pk>/', views.QuizUpdate.as_view(), name='xulyupdatetu'),
    path('xem-tu/', views.XemTu, name='xemtutheobai'),
    path('tim-tu/', views.FindAllWord, name='findallword'),
    path('random/', views.RandomWord, name='randomword'),
    path('random/quiz/', views.XuLyRandomWord, name='xulyrandomword'),

]