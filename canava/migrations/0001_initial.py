# Generated by Django 5.1.1 on 2024-09-22 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alert_message_m',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=200)),
                ('Roll_no', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=150)),
                ('gender_choice', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=150)),
            ],
        ),
    ]
