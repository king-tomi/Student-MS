from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("students", views.students, name="students"),
    path("students/<str:pk>", views.student_by_name, name="student_by_name"),
    path("courses", views.courses, name="courses"),
    path("course/<str:pk>", views.course_by_code, name="course_by_code"),
    path("lecturers", views.lecturers, name="lecturers"),
    path('lecturers/login', views.lecturer_login, name="lecturer_login"),
    path("students/login", views.student_login, name="student_login"),
    path("courses/create", views.course_create, name="create_course")
]