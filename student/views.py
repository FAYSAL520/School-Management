from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import authenticate,  login, logout
from teacher.models import Teacher
from .filters import StudentFilter, MarkFilter
from .forms import *
from .models import *




# Create your views here.

def handeLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Login!')
            return redirect('Dashboard')
        else:
            messages.error(request, 'Username OR password is incorrect')
            return redirect('handleLogin')
    return render(request, 'student/login.html')





def handelLogout(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('handleLogin')



@login_required
def Dashboard(request):
    students = Student.objects.all()
    student_count = students.count()
    teachers = Teacher.objects.all()
    teacher_count = students.count()
    context = {'student': students, 'student_count': student_count, 'teachers': teachers, 'teacher_count': teacher_count}
    return render(request, 'student/dashboard.html', context)



@login_required
def Students(request):
    students = Student.objects.all()
    student_count = students.count()
    studentFilter = StudentFilter(request.GET, queryset=students)
    students = studentFilter.qs
    context = {'student': students, 'student_count': student_count, 'studentFilter': studentFilter}
    return render(request, 'student/students_list.html', context)

@login_required
def studentProfile(request, pk):
    student = Student.objects.filter(id=pk)
    context = {'student': student}
    return render(request, 'student/student_profile.html', context)



def deleteStudent(request, pk):
    stude = get_object_or_404(Student, id=pk)
    stude.delete()
    return redirect('students')



class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('students')

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('students')






@login_required
def StudentBlood(request):
    blood = Blood.objects.all()
    context = {'blood': blood}
    return render(request, 'student/blood.html', context)

class BloodCreateView(LoginRequiredMixin, CreateView):
    model = Blood
    form_class = BloodForm
    template_name = 'student/blood_form.html'
    success_url = reverse_lazy('student_blood')

class BloodUpdateView(LoginRequiredMixin, UpdateView):
    model = Blood
    form_class = BloodForm
    template_name = 'student/blood_form.html'
    success_url = reverse_lazy('student_blood')

def deleteBlood(request, pk):
    blooddel = get_object_or_404(Blood, id=pk)
    blooddel.delete()
    return redirect('student_blood')







@login_required
def StudentGroup(request):
    group = Group.objects.all()
    context = {'group': group}
    return render(request, 'student/group.html', context)

class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'student/group_form.html'
    success_url = reverse_lazy('student_group')

class GroupUpdateView(LoginRequiredMixin, UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'student/group_form.html'
    success_url = reverse_lazy('student_group')

def deleteGroup(request, pk):
    groupdel = get_object_or_404(Group, id=pk)
    groupdel.delete()
    return redirect('student_group')







@login_required
def StudentSection(request):
    section = Section.objects.all()
    context = {'section': section}
    return render(request, 'student/section.html', context)


class SectionCreateView(LoginRequiredMixin, CreateView):
    model = Section
    form_class = SectionForm
    template_name = 'student/section_form.html'
    success_url = reverse_lazy('student_section')

class SectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Section
    form_class = SectionForm
    template_name = 'student/section_form.html'
    success_url = reverse_lazy('student_section')

def deleteSection(request, pk):
    sectiondel = get_object_or_404(Section, id=pk)
    sectiondel.delete()
    return redirect('student_section')









@login_required
def StudentGender(request):
    gender = Gender.objects.all()
    context = {'gender': gender}
    return render(request, 'student/gender.html', context)

class GenderCreateView(LoginRequiredMixin, CreateView):
    model = Gender
    form_class = GenderForm
    template_name = 'student/gender_form.html'
    success_url = reverse_lazy('student_gender')

class GenderUpdateView(LoginRequiredMixin, UpdateView):
    model = Gender
    form_class = GenderForm
    template_name = 'student/gender_form.html'
    success_url = reverse_lazy('student_gender')

def deleteGender(request, pk):
    genderdel = get_object_or_404(Gender, id=pk)
    genderdel.delete()
    return redirect('student_gender')












@login_required
def StudentClass(request):
    classes = Class.objects.all()
    context = {'classes': classes}
    return render(request, 'student/class.html', context)

class ClassCreateView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'student/class_form.html'
    success_url = reverse_lazy('student_class')

class ClassUpdateView(LoginRequiredMixin, UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'student/class_form.html'
    success_url = reverse_lazy('student_class')

def deleteClass(request, pk):
    classdel = get_object_or_404(Class, id=pk)
    classdel.delete()
    return redirect('student_class')









@login_required
def StudentSubject(request):
    subject = Subjects.objects.all()
    context = {'subject': subject}
    return render(request, 'student/subject.html', context)

class SubjectCreateView(LoginRequiredMixin, CreateView):
    model = Subjects
    form_class = SubjectForm
    template_name = 'student/subject_form.html'
    success_url = reverse_lazy('student_subject')

class SubjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Subjects
    form_class = SubjectForm
    template_name = 'student/subject_form.html'
    success_url = reverse_lazy('student_subject')

def deleteSubject(request, pk):
    classdel = get_object_or_404(Subjects, id=pk)
    classdel.delete()
    return redirect('student_subject')







@login_required
def StudentExam(request):
    exam = Exam.objects.all()
    context = {'exam': exam}
    return render(request, 'student/exam.html', context)

class ExamCreateView(LoginRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'student/exam_form.html'
    success_url = reverse_lazy('student_exam')

class ExamUpdateView(LoginRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'student/exam_form.html'
    success_url = reverse_lazy('student_exam')

def deleteExam(request, pk):
    classdel = get_object_or_404(Exam, id=pk)
    classdel.delete()
    return redirect('student_exam')








@login_required
def StudentMark(request):
    mark = Mark.objects.all()
    markFilter = MarkFilter(request.GET, queryset=mark)
    mark = markFilter.qs
    context = {'mark': mark, 'markFilter': markFilter}
    return render(request, 'student/mark.html', context)

class MarkCreateView(LoginRequiredMixin, CreateView):
    model = Mark
    form_class = MarkForm
    template_name = 'student/mark_form.html'
    success_url = reverse_lazy('student_mark')

class MarkUpdateView(LoginRequiredMixin,  UpdateView):
    model = Mark
    form_class = MarkForm
    template_name = 'student/mark_form.html'
    success_url = reverse_lazy('student_mark')

def deleteMark(request, pk):
    classdel = get_object_or_404(Mark, id=pk)
    classdel.delete()
    return redirect('student_mark')