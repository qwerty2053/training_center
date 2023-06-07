from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from course.models import Course
from student.models import Student


class Score(models.Model):
    value = models.PositiveIntegerField(
        verbose_name='Баллы',
        validators=[MinValueValidator(1, message='Value must be at least 1'),
                    MaxValueValidator(10, message='Value must be lower than 11')]
    )
    date = models.DateField(
        verbose_name='Дата',
        validators=[MinValueValidator(timezone.datetime(1900, 1, 1).date(),
                                      message='Date must be at least 1900-01-01')]
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Ученик', related_name='scores')

    def __str__(self):
        return f"{self.value} ({self.course}, {self.student})"

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
