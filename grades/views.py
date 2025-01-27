from django.db.models import Avg

from .serializers import Grades_serializer
from .models import Grade
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class GradeListView(APIView):

    def get(self, request):
        grades = Grade.objects.all()
        serializer = Grades_serializer(grades, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, id_user=None):
        Grade.objects.all().delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)


class UserGradeListView(APIView):
    def get(self, request, id_user):
        grade = Grade.objects.filter(id_user=id_user)
        serializer = Grades_serializer(grade, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, id_user):
        serializer = Grades_serializer(data=request.data)
        data = request.data
        data['id_user'] = id_user
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id_user):
        Grade.objects.filter(id_user=id_user).delete()
        return Response({"res": "Object deleted"}, status=status.HTTP_200_OK)
class UserGradeAvgView(APIView):
    def get(self, request, id_user):
        grade = Grade.objects.filter(id_user=id_user)
        if not grade.exists():
            return Response({"res": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
        avg = grade.aggregate(Avg('grade'))['grade__avg']
        return Response({"id_user": id_user, "Srednia ocen": avg}, status=status.HTTP_200_OK)