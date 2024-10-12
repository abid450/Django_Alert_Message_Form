# Generated by Django 5.1.1 on 2024-10-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canava', '0008_alter_alert_message_m_course_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert_message_m',
            name='course_name',
            field=models.CharField(choices=[('Python Programming', 'Python Programming'), ('Web Development (Python,Django)', 'Web Development (Python,Django)'), ('Grapics Design', 'Grapics Design'), ('Office Management', 'Office Management'), ('Digital Marketing', 'Digital Marketing')], max_length=150),
        ),
        migrations.AlterField(
            model_name='alert_message_m',
            name='interest',
            field=models.CharField(choices=[('Marketing', 'Marketing'), ('Design', 'Design'), ('Development', 'Development')], max_length=150),
        ),
    ]
