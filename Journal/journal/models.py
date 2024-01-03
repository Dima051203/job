from django.db import models
from django.urls import reverse


class Group(models.Model):
    name = models.CharField(
        max_length=7, help_text='Введите имя группы', unique=True, verbose_name='Группа')

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.name


class Student(models.Model):
    surname = models.CharField(
        max_length=40, help_text='Введите фамилию', verbose_name='Фамилия')
    name = models.CharField(
        max_length=40, help_text='Введите имя', verbose_name='Имя')
    number_id = models.CharField(
        max_length=7, help_text='Введите поименный номер(пример: st00001)', unique=True,)
    group = models.ForeignKey(
        'Group', on_delete=models.SET_NULL, null=True, verbose_name='Группа')
    telephone = models.CharField(
        max_length=12, help_text='Введите ваш номер телефона', unique=True,)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return 'Студент (ID {0}) {1} {2}'.format(self.number_id, self.surname, self.name)


class Teacher(models.Model):
    surname = models.CharField(
        max_length=40, help_text='Введите фамилию', verbose_name='Фамилия')
    name = models.CharField(
        max_length=40, help_text='Введите имя', verbose_name='Имя')
    thirdname = models.CharField(
        max_length=40, help_text='Введите отчество', verbose_name='Отчетство')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return '{0} {1}'.format(self.surname, self.name)


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50, help_text='Введите название факультета', verbose_name='Факультет')
    description = models.CharField(max_length=2000, help_text='Введите описание', verbose_name='Описание фаультета')

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def get_absolute_url(self):
        return reverse('faculty_name', args=[self.id])

    def __str__(self):
        return '{0} {1}'.format(self.faculty_name, self.description)


class Subject(models.Model):
    name = models.CharField(
        max_length=30, help_text='Введите название предмета', verbose_name='Предмет')
    description = models.CharField(
        max_length=100, help_text='Введите описание предмета', verbose_name='Описание предмета')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, verbose_name='Преподаватель')
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, verbose_name='Факультет')

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return '{0} {1}'.format(self.name, self.teacher)


class Grades(models.Model):
    num_of_student = models.ForeignKey(
        'Student', on_delete=models.CASCADE, verbose_name='Поименный номер')
    subject = models.ForeignKey(
        'Subject', on_delete=models.CASCADE, verbose_name='Предмет')
    g1 = models.IntegerField()
    g2 = models.IntegerField()
    g3 = models.IntegerField()
    g4 = models.IntegerField()
    g5 = models.IntegerField()
    g6 = models.IntegerField()
    g7 = models.IntegerField()
    g8 = models.IntegerField()
    g9 = models.IntegerField()
    g10 = models.IntegerField()

    class Meta:
        verbose_name = 'Успеваемость'
        verbose_name_plural = 'Успеваемости'

    def __str__(self):
        return '{0}: {1}'.format(self.num_of_student.surname, self.subject.name)
