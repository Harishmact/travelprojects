# Generated by Django 5.0 on 2024-02-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dest', '0002_hotels'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='dest/hotl'),
        ),
        migrations.AlterField(
            model_name='hotels',
            name='place',
            field=models.CharField(max_length=100),
        ),
    ]