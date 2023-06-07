from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'students_count')
    search_fields = ('name', 'description')

    def students_count(self, instance):
        return instance.students.count()
    students_count.short_description = "Количество учеников"
