# Generated by Django 4.1.1 on 2022-10-28 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(choices=[('SP', 'Service Provider'), ('C', 'Client')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(choices=[('CP', 'Concrete Pavement'), ('WP', 'Wooden Patio'), ('SP', 'Snow Shovel'), ('O', 'Others')], default='CP', max_length=50)),
                ('location', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=5000)),
                ('start_date', models.DateField(verbose_name='Tentative start date')),
                ('duration', models.IntegerField()),
                ('Identities', models.ManyToManyField(to='main_app.identity')),
            ],
        ),
        migrations.CreateModel(
            name='Quotation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.job')),
            ],
            options={
                'ordering': ['-price'],
            },
        ),
    ]
