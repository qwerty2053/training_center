from django.contrib import admin
from .models import Score


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['course', 'student', 'value', 'date']
    search_fields = ['course', 'student']
    list_filter = ['value']
