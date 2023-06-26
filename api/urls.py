from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import EmployeeViewSet, DepartmentViewSet


router = DefaultRouter()
router.register(r'departments', DepartmentViewSet, basename='departments')
router.register(r'employees', EmployeeViewSet, basename='employees')

urlpatterns = router.urls
