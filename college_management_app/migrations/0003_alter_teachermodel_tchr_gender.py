# Generated by Django 4.2.2 on 2023-06-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0002_teachermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachermodel',
            name='Tchr_Gender',
            field=models.CharField(max_length=10),
        ),
    ]
