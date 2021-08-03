from django.forms import ModelForm
from .models import Course, Lecturer, Student

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "middle_name", "last_name","age", "department", "faculty", "level","gender", "phone_no"]

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ["name","code", "description", "unit", "semester"]
        

class LecturerForm(ModelForm):
    class Meta:
        model = Lecturer
        fields = ["first_name", "middle_name", "last_name", "department", "faculty", "phone_no"]