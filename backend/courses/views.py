from django.shortcuts import render

from rest_framework import generics
from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

