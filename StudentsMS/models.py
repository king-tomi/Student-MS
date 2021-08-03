from django.db import models

# Create your models here.

class Level(models.IntegerChoices):
    FIRST = 100, "first"
    SECOND = 200, "second"
    THIRD = 300, "third"
    FOURTH = 400, "fourth"
    FIFTH = 500, "fifth"
    SIXTH = 600, "sixth"

class Student(models.Model):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, null=True, blank=True)
    age = models.IntegerField()
    date_of_brith = models.DateField()
    level = models.IntegerField(choices=Level.choices, default=Level.FIRST)
    department = models.CharField(max_length=250)
    faculty = models.CharField(max_length=250)
    matric_no = models.CharField(max_length=250)
    gender = models.CharField(max_length=6)
    cgpa = models.DecimalField(null=True, decimal_places=3, blank=True, default=0.000, max_digits=5)
    phone_no = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    class Meta:
        ordering = ("-last_name","-first_name","-middle_name")


class Course(models.Model):

    name = models.CharField(max_length=250)
    code = models.CharField(max_length=250)
    description = models.TextField()
    semester = models.CharField(max_length=6)
    unit = models.IntegerField(null=True, blank=True)
    student = models.ManyToManyField(Student,"students_offered", blank=True)

    def __str__(self) -> str:
        return self.name

class Lecturer(models.Model):

    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True)
    department = models.CharField(max_length=250)
    faculty = models.CharField(max_length=250)
    students = models.ManyToManyField(Student, "students",blank=True)
    phone_no = models.IntegerField()
    course = models.ManyToManyField(Course, blank=True)

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name} {self.middle_name}"