from django.urls import path  
from .views import *


urlpatterns = [

    # Lessons Api's endpoints

    path('lesson/list/', LessonList.as_view(), name='lesson_list'),
    path('lesson/create/', LessonCreate.as_view(), name='lesson_create'),
    path('lesson/detail/<int:pk>/', LessonDetail.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdate.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDelete.as_view(), name='lesson_delete'),
    path('lesson/filter/slug/<slug:title>/', LessonFilterBySlug.as_view(), name='lesson_filter_by_slug'),
    path('lesson/filter/status/<int:status>/', LessonFilterByStatus.as_view(), name='lesson_filter_by_status'),

    # Lesson Status Api's endpoints

    path('lesson-status/list/', LessonStatusList.as_view(), name='lesson_status_list'),
    path('lesson-status/create/', LessonStatusCreate.as_view(), name='lesson_status_create'),
    path('lesson-status/detail/<int:pk>/', LessonStatusDetail.as_view(), name='lesson_status_detail'),
    path('lesson-status/update/<int:pk>/', LessonStatusUpdate.as_view(), name='lesson_status_update'),
    path('lesson-status/delete/<int:pk>/', LessonStatusDelete.as_view(), name='lesson_status_delete'),


]