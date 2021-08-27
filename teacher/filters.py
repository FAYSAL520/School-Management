import django_filters
import self
from django import forms
from .models import *


class TeacherFilter(django_filters.FilterSet):
    class Meta:
        model = Teacher
        fields = ['gender', 'section', 'group']





