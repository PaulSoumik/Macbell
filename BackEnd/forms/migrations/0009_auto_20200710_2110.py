# Generated by Django 2.1.7 on 2020-07-10 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0008_auto_20200710_2105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='userprofile',
            new_name='user',
        ),
    ]