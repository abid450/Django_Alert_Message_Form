# Generated by Django 5.1.1 on 2024-10-08 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canava', '0016_alter_softtech_student_id_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softtech_student_id',
            name='course_name',
            field=models.CharField(choices=[('Digital Marketing', 'Digital Marketing'), ('Office Management', 'Office Management'), ('Grapics Design', 'Grapics Design'), ('Web Development (Python,Django)', 'Web Development (Python,Django)'), ('Python Programming', 'Python Programming'), ('Web Development (Django)', 'Web Development (Django)')], max_length=150),
        ),
        migrations.AlterField(
            model_name='softtech_student_id',
            name='interest',
            field=models.CharField(choices=[('Design', 'Design'), ('Marketing', 'Marketing'), ('Development', 'Development')], max_length=150),
        ),
    ]
