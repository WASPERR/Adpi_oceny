from django.urls import path

from grades.views import GradeListView, UserGradeListView

urlpatterns = [
    path('api/grades', GradeListView.as_view()),

    path('api/<int:id_user>', UserGradeListView.as_view()),
]