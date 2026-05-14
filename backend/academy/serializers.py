from rest_framework import serializers
from .models import Student, Instructor, Vehicle, Course, Enrollment, Lesson

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    
    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("La duracion debe ser mayor a 0")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio debe ser mayor o igual a 0")
        return value
    
    def validate_name(self, value):
        if not value or value.strip() == "":
            raise serializers.ValidationError("El nombre bo puede estar vacio")
        return value

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
