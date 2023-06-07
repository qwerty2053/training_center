from django.db import models
from course.models import Course


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    email = models.EmailField(verbose_name='Эл. почта')
    courses = models.ManyToManyField(Course, related_name='students', verbose_name='Курсы')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
