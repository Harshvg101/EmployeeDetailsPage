# Generated by Django 3.2 on 2025-02-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20250205_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='employee_images/'),
        ),
    ]
