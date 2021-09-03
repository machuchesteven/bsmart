from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Department(models.Model):
    class Meta:
        ordering = ["name"]
    name = models.CharField(max_length=32, blank=True, null=True)
    hod = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    class Meta:
        verbose_name_plural = "Programmes"
        ordering = ["name"]
    name = models.CharField(max_length=128, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_DEFAULT, default=1)
    duration = models.DurationField()
    intake = models.PositiveIntegerField()

    def __str__(self):
        return self.name + " : " + str(self.intake) + " intake"


class Teacher(models.Model):
    class Meta:
        ordering = ["full_name"]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128, blank=True, null=True)
    education_level = models.CharField(max_length=32, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    class Meta:
        ordering = ["course_code"]
    name = models.CharField(max_length=64, unique=True)
    course_code = models.CharField(max_length=5, unique=True)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_DEFAULT, default=1)
    program = models.ForeignKey(
        Program, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name


class Student(models.Model):
    class Meta:
        ordering = ["full_name"]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128, blank=True, null=True)
    program = models.ForeignKey(
        Program, default=1, on_delete=models.SET_DEFAULT)
    joined = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Lesson(models.Model):
    class Meta:
        ordering = ["id"]
    title = models.CharField(max_length=128, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        Teacher, default=1, on_delete=models.SET_DEFAULT)
    notes = models.FileField(upload_to='notes', blank=True, null=True)
    delivery_date = models.DateTimeField()

    def __str__(self):
        return self.title
