# Generated by Django 4.1.1 on 2023-02-20 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_job_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['-date_created']},
        ),
    ]
