from rest_framework import viewsets,permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Professor, Student, Cours
from .serializers import DepartmentSerialzer, ProfessorSerialzer, StudentSerialzer, CoursSerialzer
from rest_framework.filters import SearchFilter
from .filters import  ProfessorFilter,  StudentFilter, CoursFilter

class CoursViewSet(viewsets.ModelViewSet):
    queryset = Cours.objects.all()
    serializer_class = CoursSerialzer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CoursFilter
    search_fields = ['name']
    permission_classes = [permissions.IsAdminUser]

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerialzer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProfessorFilter
    search_fields = ['user']
    permission_classes = [permissions.IsAdminUser]

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerialzer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['user']
    permission_classes = [permissions.IsAdminUser]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerialzer

