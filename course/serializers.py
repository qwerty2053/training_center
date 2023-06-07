from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    students_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'duration', 'students_count', 'students')

    @staticmethod
    def get_students_count(obj):
        return obj.students.count()


class CourseBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']
