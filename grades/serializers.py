
from rest_framework import serializers

from grades.models import Grade

class Grades_serializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'