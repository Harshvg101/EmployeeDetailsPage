# Generated by Django 3.2 on 2025-02-03 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('employee_number', models.CharField(max_length=20, unique=True)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('talent_segment', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(max_length=100)),
                ('management_level', models.IntegerField()),
                ('home_office', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('team', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='base.employee')),
            ],
        ),
    ]
