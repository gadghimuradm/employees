from django.contrib import admin
from api.models import Position, Employee, Department


@admin.register(Position, Department)
class DefaultAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ['department']
    list_display = ['__str__', 'position', 'department']
    search_fields = ['surname']
    search_help_text = 'Поиск по фамилии'
    save_as = True
