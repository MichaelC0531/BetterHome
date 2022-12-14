# Generated by Django 4.1.1 on 2022-12-24 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_remove_job_identities_job_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='identity',
            name='identity',
            field=models.CharField(choices=[('SP', 'Service Provider'), ('C', 'Client')], default='SP', max_length=50),
        ),
        migrations.RemoveField(
            model_name='job',
            name='user',
        ),
        migrations.AlterField(
            model_name='job',
            name='work',
            field=models.CharField(choices=[('CP', 'Concrete Pavement'), ('WP', 'Wooden Patio'), ('SP', 'Snow Shovel'), ('O', 'Others')], default='CP', max_length=2),
        ),
        migrations.AddField(
            model_name='job',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
