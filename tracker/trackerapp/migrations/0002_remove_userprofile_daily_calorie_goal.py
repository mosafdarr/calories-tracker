# Generated by Django 5.1.4 on 2025-01-02 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='daily_calorie_goal',
        ),
    ]