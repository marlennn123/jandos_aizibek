from django.urls import path
from .views import DepartmentViewSet, ProfessorViewSet, StudentViewSet, CoursViewSet


urlpatterns = [
    path('', CoursViewSet.as_view({'get': 'list', 'post': 'create'}), name='cours_list'),
    path('<int:pk>/', CoursViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='student_detail'),
    path('', StudentViewSet.as_view({'get': 'list', 'post': 'create'}), name='student_list'),
    path('<int:pk>/', StudentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),name='student_detail'),
    path('', DepartmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='name_list'),
    path('<int:pk>/', DepartmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='name_detail'),
    path('', ProfessorViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('<int:pk>/', ProfessorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user_detail'),
]