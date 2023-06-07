from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

    @action(detail=True, methods=['post'])
    def enroll(self, request, pk=None, course_id=None):
        student = self.get_object()
        student.courses.add(course_id)
        return Response({'result': 'Student enrolled successfully'}, status=status.HTTP_200_OK)
