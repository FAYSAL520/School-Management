from django.conf import settings
from django.forms import DateField
from django.db import models
from django.utils.timezone import now

# Create your models here.



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




class Teacher(models.Model):
    name = models.CharField(max_length=200)
    designation = models.TextField(max_length=500)
    joining_date = models.DateField('Joining Date')
    date_of_birth = models.DateField(default=now)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    blood = models.ForeignKey(Blood, on_delete=models.CASCADE)
    Religion = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    teacher_image = models.ImageField(upload_to='teacher/', null=True, blank=True, default="default.jpg")
    address = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Teacher_Attendance(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    date = DateField(input_formats=settings.DATE_INPUT_FORMATS)

    def __str__(self):
        return self.name
