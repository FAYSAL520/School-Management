from django.urls import path
from . import views
from django.contrib import admin


admin.site.site_header = "School Management"
admin.site.site_title = "School Management System"
admin.site.index_title = "Welcome to School Management Admin Panel"

urlpatterns = [

    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),

    path('', views.Dashboard, name='Dashboard'),
    path('students', views.Students, name='students'),
    path('profile/<int:pk>', views.studentProfile, name='student_profile'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('student-edit/<int:pk>', views.PersonUpdateView.as_view(), name='person_change'),
    path('delete/<int:pk>', views.deleteStudent, name='deletestudent'),

    path('blood', views.StudentBlood, name='student_blood'),
    path('blood/add/', views.BloodCreateView.as_view(), name='student_blood_add'),
    path('blood-edit/<int:pk>', views.BloodUpdateView.as_view(), name='student_blood_change'),
    path('blood-delete/<int:pk>', views.deleteBlood, name='studentdeleteblood'),

    path('group', views.StudentGroup, name='student_group'),
    path('group/add/', views.GroupCreateView.as_view(), name='student_group_add'),
    path('group-edit/<int:pk>', views.GroupUpdateView.as_view(), name='student_group_change'),
    path('group-delete/<int:pk>', views.deleteGroup, name='studentdeletegroup'),

    path('section', views.StudentSection, name='student_section'),
    path('section/add/', views.SectionCreateView.as_view(), name='student_section_add'),
    path('section-edit/<int:pk>', views.SectionUpdateView.as_view(), name='student_section_change'),
    path('section-delete/<int:pk>', views.deleteSection, name='studentdeletesection'),

    path('gender', views.StudentGender, name='student_gender'),
    path('gender/add/', views.GenderCreateView.as_view(), name='student_gender_add'),
    path('gender-edit/<int:pk>', views.GenderUpdateView.as_view(), name='student_gender_change'),
    path('gender-delete/<int:pk>', views.deleteGender, name='studentdeletegender'),

    path('class', views.StudentClass, name='student_class'),
    path('class/add/', views.ClassCreateView.as_view(), name='student_class_add'),
    path('class-edit/<int:pk>', views.ClassUpdateView.as_view(), name='student_class_change'),
    path('class-delete/<int:pk>', views.deleteClass, name='studentdeleteclass'),

    path('subject', views.StudentSubject, name='student_subject'),
    path('subject/add/', views.SubjectCreateView.as_view(), name='student_subject_add'),
    path('subject-edit/<int:pk>', views.SubjectUpdateView.as_view(), name='student_subject_change'),
    path('subject-delete/<int:pk>', views.deleteSubject, name='studentdeletesubject'),

    path('exam', views.StudentExam, name='student_exam'),
    path('exam/add/', views.ExamCreateView.as_view(), name='student_exam_add'),
    path('exam-edit/<int:pk>', views.ExamUpdateView.as_view(), name='student_exam_change'),
    path('exam-delete/<int:pk>', views.deleteExam, name='studentdeleteexam'),

    path('mark', views.StudentMark, name='student_mark'),
    path('mark/add/', views.MarkCreateView.as_view(), name='student_mark_add'),
    path('mark-edit/<int:pk>', views.MarkUpdateView.as_view(), name='student_mark_change'),
    path('mark-delete/<int:pk>', views.deleteMark, name='studentdeletemark'),
]
