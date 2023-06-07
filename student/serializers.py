from rest_framework import serializers

from course.serializers import CourseBriefSerializer
from score.serializers import ScoreBriefSerializer
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    scores = ScoreBriefSerializer(many=True, read_only=True)
    courses = CourseBriefSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'courses', 'scores']
