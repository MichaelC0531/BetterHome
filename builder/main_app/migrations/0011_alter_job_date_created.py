# Generated by Django 4.1.1 on 2023-02-21 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_quotation_options_alter_job_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
