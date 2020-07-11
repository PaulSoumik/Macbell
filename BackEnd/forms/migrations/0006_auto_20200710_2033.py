# Generated by Django 2.1.7 on 2020-07-10 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0005_auto_20200710_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companybase',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='CompanyUserProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
