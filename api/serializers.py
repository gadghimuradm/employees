from rest_framework import serializers
from api.models import Employee, Department


class EmployeeSerializer(serializers.ModelSerializer):
    position_title = serializers.CharField(source='position.title', read_only=True)
    department_title = serializers.CharField(source='department.title', read_only=True)
    fullname = serializers.SerializerMethodField(source='get_fullname', read_only=True)

    @staticmethod
    def get_fullname(employee):
        return f'{employee.surname} {employee.name}{(" " + employee.patronymic) if employee.patronymic else ""}'

    class Meta:
        model = Employee
        fields = '__all__'
        extra_kwargs = {
            'surname': {'write_only': True},
            'name': {'write_only': True},
            'patronymic': {'write_only': True},
            'position': {'write_only': True},
            'department': {'write_only': True},
        }


class DepartmentSerializer(serializers.ModelSerializer):
    employees_count = serializers.IntegerField(read_only=True)
    total_salary = serializers.IntegerField(read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
