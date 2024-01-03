from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faculties/', views.faculties, name='faculties'),
    re_path(r'^faculty/(?P<id>\d+)$', views.faculty, name='faculty'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('faculty/', views.faculty, name='faculty'),
    path('groups/', views.groups, name='groups'),
    path('technical/', views.technical, name='technical'),
    path('page/', views.page, name='page'),
    path('grades/', views.grades, name='grades'),
    re_path(r'^grades/(?P<num_of_student>\d+)$', views.grades, name='grades'),
    path('teachers/', views.teachers, name='teachers'),
    path('personal_account/', views.personal_account, name='personal_account'),
]