# Generated by Django 4.1.1 on 2023-02-21 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_job_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quotation',
            options={'ordering': ['price']},
        ),
        migrations.AlterField(
            model_name='job',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 21, 1, 38, 36, 189893, tzinfo=datetime.timezone.utc)),
        ),
    ]
