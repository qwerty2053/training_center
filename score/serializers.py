from rest_framework import serializers

from course.serializers import CourseBriefSerializer
from .models import Score


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['course'] = instance.course.name
        rep['student'] = str(instance.student)

        return rep


class ScoreBriefSerializer(serializers.ModelSerializer):
    course = CourseBriefSerializer()

    class Meta:
        model = Score
        exclude = ['student']
