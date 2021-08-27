from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .filters import TeacherFilter
from .forms import *
from .models import *



# Create your views here.
@login_required
def Teachers(request):
    teacher = Teacher.objects.all()
    teacher_count = teacher.count()
    teacherFilter = TeacherFilter(request.GET, queryset=teacher)
    teacher = teacherFilter.qs
    context = {'teacher': teacher, 'teacher_count': teacher_count, 'teacherFilter': teacherFilter}
    return render(request, 'teacher/teachers_list.html', context)




@login_required
def teachersProfile(request, pk):
    teacher = Teacher.objects.filter(id=pk)
    context = {'teacher': teacher}
    return render(request, 'teacher/teacher_profile.html', context)

@login_required
def deleteTeacher(request, pk):
    stude = get_object_or_404(Teacher, id=pk)
    stude.delete()
    return redirect('teachers')



class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teachers')

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'teacher/teacher_form.html'
    success_url = reverse_lazy('teachers')








@login_required
def TeacherBlood(request):
    blood = Blood.objects.all()
    context = {'blood': blood}
    return render(request, 'teacher/blood.html', context)


class BloodCreateView(LoginRequiredMixin, CreateView):
    model = Blood
    form_class = BloodForm
    template_name = 'teacher/blood_form.html'
    success_url = reverse_lazy('teacher_blood')

class BloodUpdateView(LoginRequiredMixin, UpdateView):
    model = Blood
    form_class = BloodForm
    template_name = 'teacher/blood_form.html'
    success_url = reverse_lazy('teacher_blood')

@login_required
def deleteBlood(request, pk):
    blooddel = get_object_or_404(Blood, id=pk)
    blooddel.delete()
    return redirect('teacher_blood')







@login_required
def TeacherGroup(request):
    group = Group.objects.all()
    context = {'group': group}
    return render(request, 'teacher/group.html', context)

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'teacher/group_form.html'
    success_url = reverse_lazy('teacher_group')

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'teacher/group_form.html'
    success_url = reverse_lazy('teacher_group')

def deleteGroup(request, pk):
    groupdel = get_object_or_404(Group, id=pk)
    groupdel.delete()
    return redirect('teacher_group')






@login_required

def TeacherSection(request):
    section = Section.objects.all()
    context = {'section': section}
    return render(request, 'teacher/section.html', context)


class SectionCreateView(LoginRequiredMixin, CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'teacher/section_form.html'
    success_url = reverse_lazy('teacher_section')

class SectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'teacher/section_form.html'
    success_url = reverse_lazy('teacher_section')

def deleteSection(request, pk):
    sectiondel = get_object_or_404(Section, id=pk)
    sectiondel.delete()
    return redirect('teacher_section')








@login_required
def TeacherGender(request):
    gender = Gender.objects.all()
    context = {'gender': gender}
    return render(request, 'teacher/gender.html', context)

class GenderCreateView(LoginRequiredMixin, CreateView):
    model = Gender
    form_class = GenderForm
    template_name = 'teacher/gender_form.html'
    success_url = reverse_lazy('teacher_gender')


class GenderUpdateView(LoginRequiredMixin, UpdateView):
    model = Gender
    form_class = GenderForm
    template_name = 'teacher/gender_form.html'
    success_url = reverse_lazy('teacher_gender')

@login_required
def deleteGender(request, pk):
    genderdel = get_object_or_404(Gender, id=pk)
    genderdel.delete()
    return redirect('teacher_gender')




