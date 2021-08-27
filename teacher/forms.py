import self
from django import forms
from django.forms import ModelForm

from teacher.models import *


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'designation', 'joining_date', 'date_of_birth', 'gender', 'section', 'group',
                  'blood', 'Religion', 'email', 'phone', 'teacher_image', 'address', 'state', 'country']

        widgets = {
            'joining_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)

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