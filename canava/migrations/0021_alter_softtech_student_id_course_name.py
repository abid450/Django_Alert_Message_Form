# Generated by Django 5.1.1 on 2024-10-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canava', '0020_alter_softtech_student_id_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softtech_student_id',
            name='course_name',
            field=models.CharField(choices=[('Python Programming', 'Python Programming'), ('Office Management', 'Office Management'), ('Web Development (Django)', 'Web Development (Django)'), ('Digital Marketing', 'Digital Marketing'), ('Web Development (Python,Django)', 'Web Development (Python,Django)'), ('Grapics Design', 'Grapics Design')], max_length=150),
        ),
    ]
