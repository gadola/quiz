from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vi/', views.NgheDienNghia, name='nghediennghia'),
    path('en/', views.NgheDienTu, name='nghedientu'),
    path('quiz/', views.XuLy, name='xuly'),
    path('them-bai-hoc/', views.LessonFormView.as_view(), name='thembaihoc'),
    path('them-tu/', views.QuizzizFormView.as_view(), name='themtu'),

]