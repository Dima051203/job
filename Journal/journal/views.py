from django.shortcuts import render, get_object_or_404

from journal.models import Group, Faculty, Teacher, Student, Grades


def index(request):
    return render(request, 'index.html')


def main(request):
    return render(request, 'main.html')


def faculties(request):
    faculties = Faculty.objects.all().order_by('faculty_name')
    context = {'faculties': faculties}
    return render(request, 'faculties.html', context=context)


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def faculty(request, id):
    #faculties = Faculty.objects.all().order_by('faculty_name')
    obj = get_object_or_404(Faculty, pk=id)
    faculties = Faculty.objects.filter(faculty__exact=obj).order_by('faculty_name')
    context = {'faculty': obj, 'faculties': faculties}
    return render(request, 'faculty.html', context=context)


def groups(request):
    groups = Group.objects.all().order_by('name')
    context = {'groups': groups}
    return render(request, 'groups.html', context=context)


def technical(request):
    return render(request, 'technical.html')


def page(request):
    return render(request, 'page.html')


def grades(request):
    grades = Grades.objects.all()
    context = {'grades': grades}
    return render(request, 'grades.html', context=context)


def teachers(request):
    teachers = Teacher.objects.all().order_by('surname')
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context=context)


def personal_account(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'personal_account.html', context=context)
