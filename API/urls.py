from django.urls import path, include
from . import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


# quizziz_list = views.QuizzizModelViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# quizziz_detail = views.QuizzizModelViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
# })
router = DefaultRouter()
router.register(r'words', views.QuizzizModelViewSet)

urlpatterns = ([
    path('', include(router.urls)),

])