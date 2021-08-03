from django.contrib import admin
from .models import Student, Course, Lecturer

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name", "department", "level", "age", "gender", "matric_no"]
    search_fields = ["first_name", "department", "matric_no"]
    ordering = ["last_name","first_name","middle_name"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "unit"]
    ordering = ["code"]

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "middle_name", "last_name", "phone_no"]