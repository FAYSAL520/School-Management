import django_filters
import self
from django import forms
from .models import *


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['studentclass', 'gender', 'section', 'group']


class MarkFilter(django_filters.FilterSet):
    class Meta:
        model = Mark
        fields = ['student_resister_no', 'studentclass', 'subject', 'exam', 'group']

    



