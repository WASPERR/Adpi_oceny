from django.urls import path

from grades.views import GradeListView, UserGradeListView, UserGradeAvgView

urlpatterns = [
    path('api/grades', GradeListView.as_view()),

    path('api/grades/<int:id_user>', UserGradeListView.as_view()),
    path('api/grades/<int:id_user>/avg', UserGradeAvgView.as_view()),
]