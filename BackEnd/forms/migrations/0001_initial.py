# Generated by Django 2.1.7 on 2020-07-12 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CofndProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourself', models.CharField(choices=[('student', 'student'), ('enterpreneur', 'enterpreneur'), ('Businessman', 'Businessman')], max_length=100)),
                ('looking_for', models.CharField(choices=[('startup-idea', 'startup-idea'), ('startup-company', 'startup-company')], max_length=100)),
                ('industry', models.CharField(max_length=200)),
                ('join_as', models.CharField(choices=[('cofounder', 'cofounder'), ('team-member', 'team-member'), ('partner', 'partner'), ('others', 'others')], max_length=100)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('employment', models.CharField(blank=True, max_length=200)),
                ('college_name', models.CharField(max_length=200)),
                ('course_name', models.CharField(max_length=200)),
                ('passing_year', models.DateTimeField()),
                ('grade', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Cofounder_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('company_email', models.EmailField(max_length=254)),
                ('website', models.CharField(blank=True, max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CompanyUserProfile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmp_address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=200)),
                ('Businesstype', models.CharField(blank=True, max_length=200)),
                ('About_cmp', models.CharField(blank=True, max_length=500)),
                ('Company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CompanyInfo', to='forms.CompanyBase')),
            ],
        ),
        migrations.CreateModel(
            name='EduDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('college_name', models.CharField(blank=True, max_length=200)),
                ('course_name', models.CharField(blank=True, max_length=200)),
                ('passing_year', models.DateTimeField()),
                ('grade', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_education', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
            ],
        ),
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTilte', models.CharField(blank=True, max_length=200, unique=True)),
                ('Location', models.CharField(blank=True, max_length=200)),
                ('JobType', models.CharField(blank=True, choices=[('part_time', 'part_time'), ('full_time', 'full_time'), ('Freelancing_work', 'Freelancing_work'), ('Internship', 'Internship')], max_length=100)),
                ('experience', models.TextField(blank=True, max_length=400)),
                ('Last_date', models.DateTimeField()),
                ('valid', models.BooleanField(default=True)),
                ('ForCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Company_details', to='forms.CompanyBase')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_pic', models.ImageField(blank=True, upload_to='product_pics')),
                ('Prod_name', models.CharField(blank=True, max_length=200, unique=True)),
                ('Description', models.CharField(blank=True, max_length=300)),
                ('productcompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_cmp', to='forms.CompanyBase')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(choices=[('student', 'student'), ('enterpreneur', 'enterpreneur'), ('Businessman', 'Businessman')], max_length=100)),
                ('profile_as', models.CharField(choices=[('student', 'student'), ('enterpreneur', 'enterpreneur'), ('Businessman', 'Businessman'), ('Investor', 'Investor'), ('Freelancers', 'Freelancers'), ('Student Enterpreneur', 'Student Enterpreneur')], max_length=100)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('Address', models.TextField(blank=True, max_length=400)),
                ('Contact', models.BigIntegerField(unique=True)),
                ('Country', models.CharField(blank=True, max_length=100)),
                ('City', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserProfileInfo', to=settings.AUTH_USER_MODEL)),
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
                ('jobapplication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_works', to='forms.JobApplication')),
            ],
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='jobtilte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Job_adding', to='forms.JobOpening'),
        ),
    ]
