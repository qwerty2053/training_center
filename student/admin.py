from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'courses_count')
    search_fields = ('first_name', 'last_name', 'email')

    def full_name(self, instance):
        return str(instance)
    full_name.short_description = 'Полное имя'

    def courses_count(self, instance):
        return instance.courses.count()
    courses_count.short_description = 'Количество курсов'
