# Generated by Django 5.0 on 2024-01-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accom', '0003_alter_roomdetails_pimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_status', models.CharField(default='notbooked', max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('place', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=200)),
                ('cin_date', models.DateField()),
                ('cout_date', models.DateField()),
                ('comfort', models.CharField(max_length=30)),
                ('adults', models.IntegerField()),
                ('children', models.IntegerField()),
                ('noof_rooms', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='roomdetails',
            name='room_status',
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='rtype',
            field=models.CharField(max_length=30),
        ),
    ]
