from django.forms import DateField
from django.db import models
from django.utils.timezone import now
# Create your models here.



class Class(models.Model):
    studentclass = models.CharField(max_length=200)

    def __str__(self):
        return self.studentclass


class Gender(models.Model):
    gender = models.CharField(max_length=200)

    def __str__(self):
        return self.gender


class Section(models.Model):
    section = models.CharField(max_length=200)

    def __str__(self):
        return self.section


class Group(models.Model):
    group = models.CharField(max_length=200)

    def __str__(self):
        return self.group


class Blood(models.Model):
    blood = models.CharField(max_length=200)

    def __str__(self):
        return self.blood


class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.IntegerField(null=True, blank=True)
    register_no = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=now)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    studentclass = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    Religion = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    student_image = models.ImageField(upload_to='student/', null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.name)




class Student_Attendance(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    stuclass = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date = DateField()

    def __str__(self):
        return self.name





class Subjects(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self):
        return self.subject


class Exam(models.Model):
    exam = models.CharField(max_length=50)
    Note = models.TextField(null=True, blank=True)
    date = models.DateField(default=now)

    def __str__(self):
        return self.exam


class Mark(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    student_resister_no = models.CharField(max_length=999999999, null=True, blank=True)
    studentclass = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    exam_mark = models.CharField(null=True, blank=True, max_length=9000)
    assignment_mark = models.CharField(null=True, blank=True, max_length=9000)
    date = models.DateField(default=now)

    def __str__(self):
        return self.name

