from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student, Lecturer
from .forms import StudentForm, CourseForm, LecturerForm
# Create your views here.
def index(request):
    return render(request, "index.html")

def students(request):
    students = Student.objects.all()
    return render(request, "students.html", {'students': students})

def student_by_name(request, name: str):
    student = get_object_or_404(Student, first_name=name)
    return render(request, "students_detail.html", {"student": student})

def courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})

def course_by_code(request, code: str):
    course = get_object_or_404(Course, code=code)
    return render(request, "course_detail.html", {"course": course})

def lecturers(request):
    lecturers = Lecturer.objects.all()
    return render(request, "lecturer.html", {"lecturers": lecturers})

def student_login(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            return redirect("")
    else:
        form  = StudentForm()

    return render(request, "student_login.html", {'form': form})

def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)

        if form.is_valid():
            return redirect(index)
    else:
        form  = CourseForm()

    return render(request, "course_create.html", {'form': form})

def lecturer_login(request):
    if request.method == "POST":
        form = LecturerForm(request.POST)

        if form.is_valid():
            return redirect(index)
    else:
        form  = LecturerForm()

    return render(request, "lecturer_login.html", {'form': form})