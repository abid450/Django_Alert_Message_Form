# Generated by Django 5.1.1 on 2024-10-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canava', '0011_softtech_student_id_delete_alert_message_m'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softtech_student_id',
            name='biography',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='softtech_student_id',
            name='course_name',
            field=models.CharField(choices=[('Digital Marketing', 'Digital Marketing'), ('Web Development (Django)', 'Web Development (Django)'), ('Grapics Design', 'Grapics Design'), ('Python Programming', 'Python Programming'), ('Web Development (Python,Django)', 'Web Development (Python,Django)'), ('Office Management', 'Office Management')], max_length=150),
        ),
        migrations.AlterField(
            model_name='softtech_student_id',
            name='interest',
            field=models.CharField(choices=[('Development', 'Development'), ('Marketing', 'Marketing'), ('Design', 'Design')], max_length=150),
        ),
    ]
