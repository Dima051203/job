# Generated by Django 4.2.7 on 2023-12-31 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_alter_faculty_options_alter_faculty_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Факультет', 'verbose_name_plural': 'Факультеты'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]