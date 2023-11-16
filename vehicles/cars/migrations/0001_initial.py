# Generated by Django 4.2.6 on 2023-11-16 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(max_length=12, unique=True, verbose_name='Driver ID')),
                ('name', models.CharField(max_length=50, verbose_name='Driver Name')),
                ('address', models.CharField(max_length=100, verbose_name='Driver Address')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license', models.CharField(max_length=10, unique=True, verbose_name='Car License')),
                ('model', models.CharField(choices=[('BMW', 'BMW MOTORS'), ('FORD', 'FORD MOTORS'), ('GM', 'GENERAL MOTORS'), ('AUDI', 'AUDI MOTORS')], max_length=30, verbose_name='Car Model')),
                ('year', models.IntegerField(verbose_name='Car Make Year')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.person')),
            ],
        ),
    ]