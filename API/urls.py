from django.urls import path, include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


lesson_list = views.LessonModelViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

quizziz_detail = views.QuizzizModelViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})
router = DefaultRouter()
router.register(r'words', views.QuizzizModelViewSet)
router.register(r'lessons', views.LessonModelViewSet)

urlpatterns = ([
    path('', include(router.urls)),
    path('lesson/', views.lessons_list , name="wl"),
    path('lesson/<int:pk>/',views.words_detail, name="wd"),

])