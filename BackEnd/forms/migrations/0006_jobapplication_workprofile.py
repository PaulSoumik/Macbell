# Generated by Django 2.1.7 on 2020-07-12 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forms', '0005_auto_20200713_0206'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applyas', models.CharField(choices=[('Student', 'Student'), ('Employee', 'Employee')], max_length=100)),
                ('college_name', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('passing_year', models.DateTimeField()),
                ('grade', models.IntegerField(default=0)),
                ('aboutapplicant', models.TextField(max_length=400)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_details', to=settings.AUTH_USER_MODEL)),
                ('jobtilte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Job_adding', to='forms.JobOpening')),
            ],
        ),
        migrations.CreateModel(
            name='WorkProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company_name', models.CharField(blank=True, max_length=200)),
                ('Post', models.CharField(blank=True, max_length=100)),
                ('Start_date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(blank=True)),
                ('jobapplication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workprofile', to='forms.JobApplication')),
            ],
        ),
    ]
