# Generated by Django 5.0 on 2024-01-20 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accom', '0007_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookroom',
            name='user_name',
        ),
    ]