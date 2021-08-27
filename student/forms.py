from django import forms
from django.forms import ModelForm

from student.models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})





class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = "__all__"

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(ExamForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})





class MarkForm(ModelForm):
    class Meta:
        model = Mark
        fields = "__all__"

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(MarkForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})




class BloodForm(ModelForm):
    class Meta:
        model = Blood
        fields = "__all__"


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = "__all__"


class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = "__all__"


class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = "__all__"


class SubjectForm(ModelForm):
    class Meta:
        model = Subjects
        fields = "__all__"

