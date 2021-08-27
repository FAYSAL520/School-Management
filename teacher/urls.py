from django.urls import path
from . import views




urlpatterns = [
    path('', views.Teachers, name='teachers'),
    path('profile/<int:pk>', views.teachersProfile, name='teacher_profile'),

    path('add/', views.PersonCreateView.as_view(), name='teacher_add'),
    path('teacher-edit/<int:pk>', views.PersonUpdateView.as_view(), name='teacher_change'),
    path('delete/<int:pk>', views.deleteTeacher, name='teacherdelete'),

    path('blood', views.TeacherBlood, name='teacher_blood'),
    path('blood/add/', views.BloodCreateView.as_view(), name='teacher_blood_add'),
    path('blood-edit/<int:pk>', views.BloodUpdateView.as_view(), name='teacher_blood_change'),
    path('blood-delete/<int:pk>', views.deleteBlood, name='teacherdeleteblood'),

    path('group', views.TeacherGroup, name='teacher_group'),
    path('group/add/', views.GroupCreateView.as_view(), name='teacher_group_add'),
    path('group-edit/<int:pk>', views.GroupUpdateView.as_view(), name='teacher_group_change'),
    path('group-delete/<int:pk>', views.deleteGroup, name='teacherdeletegroup'),

    path('section', views.TeacherSection, name='teacher_section'),
    path('section/add/', views.SectionCreateView.as_view(), name='teacher_section_add'),
    path('section-edit/<int:pk>', views.SectionUpdateView.as_view(), name='teacher_section_change'),
    path('section-delete/<int:pk>', views.deleteSection, name='teacherdeletesection'),

    path('gender', views.TeacherGender, name='teacher_gender'),
    path('gender/add/', views.GenderCreateView.as_view(), name='teacher_gender_add'),
    path('gender-edit/<int:pk>', views.GenderUpdateView.as_view(), name='teacher_gender_change'),
    path('gender-delete/<int:pk>', views.deleteGender, name='teacherdeletegender'),
]
