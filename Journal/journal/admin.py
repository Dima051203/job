from django.contrib import admin

from journal.models import Group, Student, Teacher, Faculty, Subject, Grades

admin.site.register(Group),
#admin.site.register(Student),
#admin.site.register(Teacher),
#admin.site.register(Faculty),
#admin.site.register(Subject),
#admin.site.register(Grades),


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'number_id', 'group')
    list_per_page = 10
    search_fields = ('surname',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'thirdname')
    list_per_page = 10
    search_fields = ('surname',)


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'description')


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'faculty')
    list_per_page = 10
    search_fields = ('name', 'faculty__faculty_name')


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10')
    list_per_page = 10
    search_fields = ('num_of_student__surname',)
