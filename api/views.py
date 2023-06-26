from django.db.models import Count, Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from api.models import Employee, Department
from api.serializers import DepartmentSerializer, EmployeeSerializer
from api.paginators import DefaultPageNumberPagination


class DepartmentViewSet(ModelViewSet):
    """Departments ViewSet"""
    queryset = Department.objects.annotate(
        employees_count=Count('employees'),
        total_salary=Sum('employees__salary')
    )
    serializer_class = DepartmentSerializer
    http_method_names = ['get']


class EmployeeViewSet(ModelViewSet):
    """Employees ViewSet"""
    def get_queryset(self):
        queryset = Employee.objects.all()
        if self.request.query_params.get('department'):
            queryset = queryset.filter(department__id=self.request.query_params.get('department'))
        if self.request.query_params.get('surname'):
            queryset = queryset.filter(surname__icontains=self.request.query_params.get('surname'))
        return queryset.select_related('position', 'department').only('position__title', 'department__title')

    serializer_class = EmployeeSerializer
    pagination_class = DefaultPageNumberPagination
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
