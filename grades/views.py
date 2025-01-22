from django.shortcuts import render
from grades.serializers import Gradeserializer
from grades.models import Grade
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class GradeListView(APIView):

    def get(self, request, *args, **kwargs):
        grades = Grade.objects.all()
        serializer = Gradeserializer(grades, many=True)

        custom_data = {
            'results': serializer.data,
            'message': 'Successfully fetched all grades'
        }

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        data = {
            'grade': request.data.get['grade'],
            'created_at': request.data.get['created_at'],
            'id_user': request.user.id
        }

        serializer = Gradeserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserGradeListView(APIView):
    def get_object(self, grade_id, user_id):
        try:
            return Grade.objects.get(id=grade_id, user_id=user_id)
        except Grade.DoesNotExist:
            return None
    def get(self, request, grade_id, *args, **kwargs):
        grade = self.get_object(grade_id, request.user.id)
        if not grade:
            return Response({"res": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = Gradeserializer(grade)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, grade_id, *args, **kwargs):
        grade = self.get_object(grade_id, request.user.id)
        if not grade:
            return Response({"res": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        grade.delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)