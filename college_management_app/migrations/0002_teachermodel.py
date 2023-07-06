# Generated by Django 4.2.2 on 2023-06-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tchr_Age', models.IntegerField()),
                ('Tchr_Address', models.CharField(max_length=255)),
                ('Tchr_Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=2)),
                ('Tchr_Phone', models.IntegerField()),
                ('Tchr_Image', models.ImageField(null=True, upload_to='image/')),
                ('Tchr_Joining_Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]