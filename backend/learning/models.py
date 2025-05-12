from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
