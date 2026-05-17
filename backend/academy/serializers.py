from rest_framework import serializers
from .models import Student, Instructor, Vehicle, Course, Enrollment, Lesson

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StudentPictureSerializer(serializers.ModelSerializer):
    def validate_profile_picture(self, value):
        # TODO(actividad): Implementar validaciones de archivo (tamano y tipo MIME).
        # Ejemplo: permitir image/jpeg e image/png y limitar a 2MB.
        
        allowed_types = ['image/jpeg', 'image/png', 'image/webp']

        if value.content_type not in allowed_types:
            raise serializers.ValidationError(
                "Tipo de archivo no permitido. Solo son permitidos los formatos JPEG, PNG o WEBP."
            )

        max_size = 2 * 1024 * 1024  # 2MB
        if value.size > max_size:
            raise serializers.ValidationError(
                "El tamaño del archivo excede el límite de 2MB."
            )
        
        return value

    class Meta:
        model = Student
        fields = ['profile_picture']

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

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
