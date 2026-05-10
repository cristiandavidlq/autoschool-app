from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    StudentViewSet, InstructorViewSet, VehicleViewSet,
    CourseViewSet, EnrollmentViewSet, LessonViewSet
)

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')
# TODO: Register the other viewsets

urlpatterns = [
    path('', include(router.urls)),
]
