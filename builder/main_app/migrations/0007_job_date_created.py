# Generated by Django 4.1.1 on 2023-02-20 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_quotation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_created',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
