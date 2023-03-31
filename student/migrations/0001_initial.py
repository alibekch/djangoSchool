# Generated by Django 4.1.7 on 2023-03-31 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('letter', models.CharField(max_length=1)),
                ('school_year', models.DateField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.school')),
                ('subjects', models.ManyToManyField(to='main.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.klass')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_name', models.CharField(max_length=32)),
                ('start_time', models.DateField()),
                ('end_time', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Оценка')),
                ('grade_value', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Ученик', to='student.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Учитель', to='employee.teacher')),
            ],
        ),
    ]
