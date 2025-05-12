from django.urls import path
from .views import CourseListView, LessonListView

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('lessons/', LessonListView.as_view(), name='lesson-list'),
]
